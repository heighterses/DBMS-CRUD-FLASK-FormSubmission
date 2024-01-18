from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DATABASE INTEGRATION
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///book_shelf.db"
db = SQLAlchemy(app)


class BOOKshelf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()

# APPLICATION CODE
all_books = []


@app.route('/')
def home():
    return render_template('index.html', books=[])


@app.route('/add', methods=["POST", "GET"])
def add_book():
    if request.method == "POST":
        data = request.form
        title = data["name"]
        author = data["author"]
        rating = data["rating"]

        # new_book = {
        #     "title": data["name"],
        #     "author": data["author"],
        #     "rating": data["rating"]
        # }
        # all_books.append(new_book)

        return redirect(url_for('home'))

    return render_template('add_book.html')


if __name__ == '__main__':
    app.run(debug=True)
