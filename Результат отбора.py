from flask import Flask, url_for, request
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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
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
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="SecondName">
                                    <input type="password" class="form-control" id="password" placeholder="Введите имя" name="FirstName">
                                    <div class="form-group">
                                        <label for="classSelect">Кокое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Послевузовское</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Какие у Вас есть профессии?</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Повар</label>
                                    </div>

                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы решили записаться в добровольцы?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы жить на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    text = ['Хорошая планета!',
            'Отличная планета!!',
            'Моя любимая планета!!!']
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Предлагаю {planet_name}!</title>
                  </head>
                  <body>
                    <h1>Моё предложение: {planet_name}</h1>
                  <div class="alert alert-primary" role="alert">
                    Хорошая планета!
                  </div>
                  <div class="alert alert-danger" role="alert">
                    Отличная планета!!
                  </div>
                  <div class="alert alert-success" role="alert">
                    Моя любимая планета!!!
                  </div>
                  </body>
            '''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                  <div class="alert alert-primary" role="alert">
                    Претендента на участие в миссии {nickname}:
                  </div>
                  <div class="alert alert-danger" role="alert">
                    Поздравляем! Ваш рейтинг после {level} отбора
                  </div>
                  <div class="alert alert-success" role="alert">
                    составляет {rating}!
                  </div>
                  <div class="alert alert-light" role="alert">
                    Желаем удачи!
                  </body>
            '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
