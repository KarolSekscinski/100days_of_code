from flask import Flask, render_template
import datetime
import requests

AGE_URL = "https://api.agify.io/"
GENDER_URL = "https://api.genderize.io"

app = Flask(__name__)


def age(body):
    response = requests.get(url=AGE_URL, params=body)
    user_age = response.json()['age']
    return user_age


def gender(body):
    response = requests.get(url=GENDER_URL, params=body)
    user_gender = response.json()['gender']
    return user_gender


@app.route('/')
def home():

    footer = f"{datetime.datetime.now().year}"
    return render_template("index.html", footer=footer)


@app.route('/guess/<name>')
def guess(name):

    body = {
        "name": name
    }
    user_age = age(body)
    user_gender = gender(body)
    return render_template("index.html", name=name.capitalize(), age=user_age, gender=user_gender )

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    data = response.json()
    return render_template("blog.html", posts=data)

if __name__ == '__main__':
    app.run(debug=True)


