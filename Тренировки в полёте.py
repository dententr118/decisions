from flask import Flask, url_for, request, render_template
from http.server import HTTPServer, CGIHTTPRequestHandler

app = Flask(__name__)


@app.route('/')
@app.route('/index/<titl>')
def index(titl=''):
    return render_template('index.html', title=titl)


@app.route('/training/<prof>')
def training(prof=''):
    return render_template('training.html', profile=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
