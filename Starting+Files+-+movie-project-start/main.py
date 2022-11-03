from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import requests

app = Flask(__name__)

Bootstrap(app)

app.config['SECRET_KEY'] = 'this is secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


class AddMovie(FlaskForm):
    title = StringField("Movie Title",
                        validators=[DataRequired(),
                                    Length(min=1, max=150, message="Tell me what you felt after watching movie")])
    # year = StringField("Released Year", validators=[DataRequired()])
    # description = StringField("Summary for a movie", validators=[DataRequired()])
    # rating = StringField("Rating", validators=[DataRequired()])
    # ranking = StringField("Ranking", validators=[DataRequired()])
    # img_url = StringField("Insert a URL of Movie Poster", validators=[DataRequired(), URL()])
    submit = SubmitField('Submit')


class RateMovieForm(FlaskForm):
    rating = StringField("Rating", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField("Done")


app.app_context().push()
db.create_all()



@app.route('/')
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        parameters = {
            "api_key": "12345678",
            "language": "en-US",
            "query": form.title.data
        }
        data = requests.get("https://api.themoviedb.org/3/search/movie", params=parameters).json()["results"]
        return render_template('select.html', options=data)

    return render_template("add.html", form=form)


@app.route('/edit', methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        data = requests.get(movie_api_url, params={"api_key": "12345678", "language": "en-US"}).json()
        image = requests.get(f"{movie_api_url}/images", params={"api_key": "12345678", "language": "en-US"}).json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=image["img_url"],
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit"))



if __name__ == '__main__':
    app.run(debug=True)
