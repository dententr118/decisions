from flask import Flask, url_for
from http.server import HTTPServer, CGIHTTPRequestHandler

app = Flask(__name__)


@app.route("/")
def name_of_operation():
    return 'Миссия Колонизация Марса'


@app.route("/index")
def apple():
    return 'И на Марсе будут яблони цвести!'


@app.route("/promotion")
def promotion():
    text = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!',
            'Присоединяйся!']
    return '<br>'.join(text)


@app.route("/image_mars")
def mars_image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                  <body>
                    <img src="/static/img/riana.jpg" alt="здесь должна была быть картинка, но не нашлась">
                  <body>
                    <br>Вот она какая, красная планета.<br>
            '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
