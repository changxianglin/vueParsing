from flask import Flask
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager
app = Flask(__name__)
Manager = Manager(app)


@app.route('/', methods = ['GET', 'POST'])
def index():
    return '<h1>Hello, World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/res')
def res():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/red')
def red():
    return redirect('http://www.example.com')


@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name


if __name__ == '__main__':
    # app.run(debug=True)
    Manager.run()