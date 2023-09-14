from flask import Flask, render_template, request
import requests
import smtplib

my_email = "karoltestemail@gmail.com"
my_password = "ziyvcqtldcebitne"
URL = "https://api.npoint.io/eb6cd8a5d783f501ee7d"

app = Flask(__name__)


def get_data():
    response = requests.get(url=URL)
    data = response.json()
    return data


def get_single_post(blog_id):
    blog_posts = get_data()
    for post in blog_posts:
        if post['id'] == int(blog_id):
            return post
    return None


@app.route('/')
def home():
    blog_posts = get_data()
    return render_template("index.html", posts=blog_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", contacted=False)
    elif request.method == "POST":
        message = (f"Subject:New Message\n\nName: {request.form['name']}\nEmail: {request.form['email']}\n"
                   f"Phone Number: {request.form['phone']}\nMessage: {request.form['message']}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=message)
        return render_template("contact.html", contacted=True)


@app.route('/post/<blog_id>')
def single_post(blog_id):
    post_data = get_single_post(blog_id)
    return render_template("post.html", post=post_data)


if __name__ == "__main__":
    app.run(debug=True)