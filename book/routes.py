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
    items = Item.query.all()
    return render_template("books.html", items = items)