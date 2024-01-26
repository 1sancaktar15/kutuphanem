from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key= True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    genre = db.Column(db.String(length=30), nullable=False, unique=True)
    page = db.Column(db.Integer(), nullable=False,unique=True)
    blurb = db.Column(db.String(length=1024), nullable=False, unique=True)



if __name__ == '__main__':
    app.run(debug=True, port=5000)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/about")
def about_page():
    return "<h1>About Page</h1>"

#dinamik route
@app.route("/favourites/<username>")
def favourites_page(username):
    return f'<h1>Favourites page for the user {username}</h1>'


@app.route("/books")
def kitap_page():
    items = [
    {'id': 1, 'name': 'Gece Yarısı Kütüphanesi', 'genre': 'Fantastik Kurgu', 'page': 283},
    {'id': 2, 'name': 'Zafer Sızlanarak Kazanılmaz', 'genre': 'Kişisel Gelişim', 'page': 480},
    {'id': 3, 'name': 'Eğitilmemiş Zihin', 'genre': 'Psikoloji', 'page': 324}
    ]
    return render_template("books.html", items = items)



