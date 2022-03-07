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
                    <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась">
                  <body>
                    <br>Вот она какая, красная планета.<br>
            '''


@app.route("/promotion_image")
def promotion_image():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />

                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась">
                        <p style="font-size: 120%; font-family: monospace; color: #cd66cc">Вот она какая, красная планета.</p>
                        <p style="font-size: 120%; font-family: monospace; color: #ff0000">Человечество вырастает из детства.</p>
                        <p style="font-size: 120%; font-family: monospace; color: #008000">Человечеству мала одна планета.</p>
                        <p style="font-size: 120%; font-family: monospace; color: #0000ff">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                        <p style="font-size: 120%; font-family: monospace; color: #8b00ff">И начнем с Марса!</p>
                        <p style="font-size: 120%; font-family: monospace; color: #ffff00">Присоединяйся!</p>
                      <body>
                '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
