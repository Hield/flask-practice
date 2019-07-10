from flask import (
    Blueprint, flash, g, request, jsonify, Response
)
from werkzeug.exceptions import abort
from message_board.model.message import get_messages_with_version, add_message, xmlify
from urllib.parse import urlparse

bp = Blueprint('message', __name__)


@bp.route('/message', methods=['GET'])
def list_messages():
    version = request.args.get('version')
    if version is None:
        version = 2
    else:
        try:
            version = int(version)
        except ValueError:
            abort(400, 'Invalid version')

    messages = get_messages_with_version(version)
    if version == 1:
        return jsonify(messages)
    
    format_type = request.args.get('format')

    if format_type == 'xml':
        return Response(xmlify(messages), mimetype='text/xml')
        
    return jsonify(messages)

@bp.route('/message', methods=['POST'])
def create_message():
    payload = request.json
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

    if error is not None:
        abort(400, error)

    add_message(payload)
    return Response(status=201)