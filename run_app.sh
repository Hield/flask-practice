#!/bin/bash
pip install -r requirements.txt
export FLASK_APP=message_board
export FLASK_ENV=development
flask run