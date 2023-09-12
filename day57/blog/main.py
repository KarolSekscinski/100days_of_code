from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    post = Post()
    return render_template("index.html", blog_posts=post.posts)


@app.route('/post/<blog_id>')
def single_post(blog_id):
    post = Post()
    one_post = post.get_single_post(blog_id)
    return render_template("post.html", post=one_post)


if __name__ == "__main__":
    app.run(debug=True)
