from flask import Flask, url_for, request, render_template
from http.server import HTTPServer, CGIHTTPRequestHandler
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/')
@app.route('/index/<titl>')
def index(titl=''):
    return render_template('index.html', title=titl)


@app.route('/training/<prof>')
def training(prof=''):
    return render_template('training.html', profile=prof)


@app.route('/list_prof/<num>')
def list_prof(num=''):
    with open('static/json/profiles.json', 'rt', encoding='utf8') as f:
        new_list = json.loads(f.read())
    return render_template('professions.html', param=num, prof_list=new_list)


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    list = {'title': 'анкета',
            'surname': 'Примо',
            'name': 'Эль',
            'education': 'начальное',
            'profession': 'нет',
            'sex': 'male',
            'motivation': 'кубки',
            'ready': 'yes'}
    return render_template('answers.html', listik=list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
