from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# flask is a framework
# flask is a microframework that is designed to be used as a standalone application or as a small
# component in larger applications

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

def make_italic(function):
    def wrapper():
        return "<i>" + function() + "</i>"
    return wrapper


app = Flask(__name__)


# __name__ is a special variable that is set to the name of the module in which it is used
# if the module is the main module (the one with the name __main__) then __name__ is set to '__main__',
# means that __name__ is the name of the module that is running
@app.route('/')
# @app.route is a decorator that tells the application which URL should call the associated function
def index():
    return "<h1>hello world</h1>" \
           "<h2>This is my first flask app</h2>" \


@app.route('/bye')
@make_bold
def bye():
    return "bye"


@app.route('/username/<name>/<int:age>')
def greet(name, age):
    return "hello " + name + " you are " + str(age) + " years old"


if __name__ == '__main__':
    app.run(debug=True)


