from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


url='https://api.themoviedb.org/3/movie/550?api_key=396be4338b398488a35e17ff5ba92c18'

API_KEY= "API_KEY"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key go here'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies_collections.db"
db = SQLAlchemy(app)
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Float, nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"<id={self.id}, title={self.title}>, description={self.description}, rating={self.rating}," \
               f"ranking={self.ranking}, review={self.review}, img_url={self.img_url}"


db.create_all()

new_one = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's "
                "sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller"
                " leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

#db.session.add(new_one)
db.session.commit()

@app.route("/", methods=['GET'])
def home():
    all_movies = Movie.query.all()
    print(all_movies)
    return render_template("index.html", movies=all_movies)

@app.route('/delete',methods=['GET'])
def delete_post():
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect('/')

class Form(FlaskForm):
    rating = StringField( 'Your rating out of 10', validators=[DataRequired()])
    review = StringField('Your review goes here', validators=[DataRequired()])
    Done= SubmitField('Done')
@app.route('/edit/', methods=['GET', 'POST'])
def edit_movie():
    form= Form()
    if request.method == "POST":
        if form.validate_on_submit():
            movie_id = request.args.get('id')
            print(movie_id)
            movie_to_update = Movie.query.get(movie_id)
            movie_to_update.rating = form.rating.data
            movie_to_update.review =form.review.data
            db.session.commit()
            return redirect('/')
    return render_template('edit.html', form=form)

class Add_movie(FlaskForm):
    title = StringField( 'Movie Title', validators=[DataRequired()])
    submit= SubmitField('Add more movies')

@app.route('/add',methods=['GET', 'POST'] )
def add_movie():
   
    form = Add_movie()
    if request.method == 'POST':
        # if form.validate_on_submit():
        parameter = {
            'api_key': '3API_KEY',
            'query': f'{form.title.data}'}
        URL = 'https://api.themoviedb.org/3/search/movie'
        response = requests.get(URL, params=parameter).json()['results']
       
        return render_template('select.html', post=response)
    return render_template('add.html', form=form)

@app.route('/find')
def find_movie():
    movie_id = request.args.get('id')
    print(movie_id)
    parameter = {
        'api_key': 'API_KEY'
    }
    URL = f'https://api.themoviedb.org/3/movie/{movie_id}?'
    pic_url='https://image.tmdb.org/t/p/w500/'
    data = requests.get(URL, params=parameter).json()
    new_movie = Movie(
        title=data["title"],
        year=data["release_date"].split("-")[0],
        rating= 9.2,
        ranking =5,
        review= data['popularity'],
        img_url=f"{pic_url}/{data['poster_path']}",
        description=data["overview"]
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit_movie", id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
