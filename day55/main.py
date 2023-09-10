from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return "<b>" + func() + "<b/b"
    return wrapper


def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "<em/>"
    return wrapper


def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "<u/>"
    return wrapper


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)