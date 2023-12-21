from flask import Flask
from flask import render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/books")
def kitap_page():
    items = [
    {'id': 1, 'name': 'Gece Yarısı Kütüphanesi', 'genre': 'Fantastik Kurgu', 'page': 283},
    {'id': 2, 'name': 'Zafer Sızlanarak Kazanılmaz', 'genre': 'Kişisel Gelişim', 'page': 480},
    {'id': 3, 'name': 'Eğitilmemiş Zihin', 'genre': 'Psikoloji', 'page': 324}
    ]
    return render_template("books.html", items = items)

