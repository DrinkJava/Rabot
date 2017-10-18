"""
Server for chatbot.
"""
import curse
from flask import Flask
from flask import request
from flask import json
import re

modules = {":curse" : curse.curse}

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recv_data():
    data = request.get_data()
    data = json.loads(data)
    return parse(data)

def parse(data):
    body = data['body']
    cmds = [word for word in body.split() if word.startswith(":")]
    for cmd in cmds:
        fn = modules.get(cmd, -1)
        if fn == -1:
            continue
        return fn()
