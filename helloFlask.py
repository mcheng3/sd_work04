from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def helloWorld():
    return "Hello, World!"

@my_app.route('/hello')
def hello():
    return "hello"

@my_app.route('/world')
def world():
    return "<h1>world</h1>"

if __name__ == '__main__':
    my_app.run()

my_app.debug = True
