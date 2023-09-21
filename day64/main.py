from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

URL = "https://api.themoviedb.org/3/search/movie"
API_KEY = "YOUR API KEY"
TOKEN = "YOUR TOKEN"
URL_DETAILS = "https://api.themoviedb.org/3/movie"
URL_IMAGE = "https://image.tmdb.org/t/p/w400"
headers = {
    "accept": "application/json",
    "Authorization": f"{TOKEN}"
}
class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddMovie(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add movie')


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"

db.init_app(app)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String, nullable=True)
    img_url: Mapped[str] = mapped_column(String, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()

    for i in range(len(result)):
        result[i].ranking = len(result) - i
    db.session.commit()

    return render_template("index.html", movies=result)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    if form.validate_on_submit():
        movie_id = request.args.get('id')
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.rating = form.data['rating']
        movie_to_update.review = form.data['review']
        db.session.commit()
        return redirect(url_for('home'))
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)
    return render_template("edit.html", movie=movie_selected, form=form)


@app.route('/delete', methods=["GET"])
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)

    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        title = form.data['title']
        params = {
            "query": title
        }
        response = requests.get(url=URL, headers=headers, params=params)
        movies = response.json()['results']
        return render_template("select.html", movies=movies)

    return render_template("add.html", form=form)

@app.route('/find_movie')
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{URL_DETAILS}/{movie_api_id}"
        response = requests.get(url=movie_api_url, headers=headers)
        data = response.json()
        new_movie = Movie(
            title=data['original_title'],
            img_url=f"{URL_IMAGE}/{data['poster_path']}",
            year=data['release_date'].split("-")[0],
            description=data['overview']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
