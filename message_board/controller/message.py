from flask import (
    Blueprint, flash, g, request, jsonify, Response
)
from werkzeug.exceptions import abort
from message_board.model.message import get_messages_with_version, add_message, check_message_validity, xmlify

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
    error = check_message_validity(payload)

    if error is not None:
        abort(400, error)

    add_message(payload)
    return Response(status=201)