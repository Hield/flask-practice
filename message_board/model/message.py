from xml.etree.ElementTree import Element, SubElement, tostring
from urllib.parse import urlparse

MESSAGES = [
    {
        'title': 'My first message',
        'content': 'Hello World',
        'sender': 'Hieu Le',
        'url': 'https://www.google.com/'
    },
    {
        'title': 'A message from somewhere',
        'content': "It's a secret",
        'sender': 'Tony Stark',
        'url': 'https://www.bbc.co.uk/'
    }
]

def get_messages():
    return MESSAGES.copy()

def add_message(message):
    MESSAGES.append(message)

def to_version_one(messages):
    return [{
        'title': x['title'],
        'content': x['content'],
        'sender': x['sender']
    } for x in messages]

def get_messages_with_version(version=2):
    if version == 1:
        return to_version_one(get_messages())
    elif version == 2:
        return get_messages()
    return []

def xmlify(messages):
    root = Element('messages')

    for message in messages:
        child = SubElement(root, 'message')
        title = SubElement(child, 'title')
        title.text = message['title']
        content = SubElement(child, 'content')
        content.text = message['content']
        sender = SubElement(child, 'sender')
        sender.text = message['sender']
        url = SubElement(child, 'url')
        url.text = message['url']

    return tostring(root, encoding='utf8', method='xml')

def check_message_validity(payload):
    error =  None
    if 'title' not in payload:
        error = 'Missing title'
    elif 'content' not in payload:
        error = 'Missing content'
    elif 'sender' not in payload:
        error = 'Missing sender'
    elif 'url' not in payload:
        error = 'Missing url'
    elif not isinstance(payload['title'], str) or len(payload['title']) > 20:
        error = 'Invalid title'
    elif not isinstance(payload['content'], str) or len(payload['content']) > 100:
        error = 'Invalid content'
    elif not isinstance(payload['sender'], str) or len(payload['sender']) > 20:
        error = 'Invalid sender'
    elif not isinstance(payload['url'], str):
        error = 'Invalid url'
    else:
        try:
            result = urlparse(payload['url'])
            if not all([result.scheme, result.netloc]):
                error = 'Invalid url'
        except ValueError:
            error = 'Invalid url'

    return error