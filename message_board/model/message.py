from xml.etree.ElementTree import Element, SubElement, tostring

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
