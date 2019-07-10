import types

from werkzeug.wsgi import DispatcherMiddleware
from pysimplesoap.server import SoapDispatcher, WSGISOAPHandler
from message_board.model.message import check_message_validity, add_message

def hello(name):
    return "Hello, " + str(name)

def create_message(title, content, sender, url):
    payload = {
        'title': title,
        'content': content,
        'sender':sender,
        'url': url
    }
    error = check_message_validity(payload)
    if error is not None:
        raise Exception(error)
    add_message(payload)

    return 'Success'

def create_soap_dispatcher():
    dispatcher = SoapDispatcher(
        name="Soap",
        location="http://localhost:5000/",
        action="http://localhost:5000"
    )
    dispatcher.register_function('Hello', hello,
        returns={'message': str},
        args={'name': str})

    dispatcher.register_function('CreateMessage', create_message,
        returns={'result': str},
        args={'title': str, 'content': str, 'sender': str, 'url': str})

    return dispatcher



def create_soap_handler():
    handler = WSGISOAPHandler(create_soap_dispatcher())

    # A hack to make sure the request turned to string if it's bytes
    def do_post(self, environ, start_response):
        length = int(environ['CONTENT_LENGTH'])
        request = environ['wsgi.input'].read(length)
        if isinstance(request, bytes):
            request = request.decode('utf8')
        response = self.dispatcher.dispatch(request)
        start_response('200 OK', [('Content-Type', 'text/xml'), ('Content-Length', str(len(response)))])
        return [response]
    
    handler.do_post = types.MethodType(do_post, handler)

    return handler