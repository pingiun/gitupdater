import os
import subprocess
import hashlib
import hmac
import hashlib
import json

import git

from flask import Flask, request

app = Flask(__name__)

app.config.from_envvar('GITUPDATER_SETTINGS')


@app.route('/_/githubwebhook', methods=['GET', 'POST'])
def handle_webhook():
    if request.method == 'GET':
        return 'Method Not Allowed', 405

    payload = json.loads(request.data.decode('utf-8'))

    if 'GITHUB_SHARED_SECRET' in app.config:
        if not request.headers.get('X-Hub-Signature'):
            return 'Unauthorized', 401
        hmacdigest = 'sha1=' + hmac.new(app.config['GITHUB_SHARED_SECRET'],
                              request.data, hashlib.sha1).hexdigest()
        if hmac.compare_digest(hmacdigest,
                               request.headers.get('X-Hub-Signature')) == False:
            return 'Unauthorized', 401

    if request.headers.get('X-GitHub-Event') == 'ping':
        return json.dumps({'msg': 'pong'})

    if request.headers.get('X-Github-Event') != 'push':
        return 'Bad Request', 400

    os.chdir(app.config['GIT_REPO'])
    g = git.cmd.Git(app.config['GIT_REPO'])
    print(g.pull())
    if 'POST_PULL' in app.config:
        print(subprocess.check_output(app.config['POST_PULL']))
    return 'OK', 200
