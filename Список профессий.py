from flask import Flask, url_for, request, render_template
from http.server import HTTPServer, CGIHTTPRequestHandler
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index/<titl>')
def index(titl=''):
    return render_template('index.html', title=titl)


@app.route('/training/<prof>')
def training(prof=''):
    return render_template('training.html', profile=prof)


@app.route('/list_prof/<num>')
def list_prof(num=''):
    with open('profiles.json', 'rt', encoding='utf8') as f:
        new_list = json.loads(f.read())
    return render_template('professions.html', param=num, prof_list=new_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
