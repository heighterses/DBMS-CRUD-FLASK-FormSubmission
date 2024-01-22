from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DATABASE INTEGRATION
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///book_shelf.db"
db = SQLAlchemy(app)


class BOOKS(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, primary_key=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()

# APPLICATION CODE
all_books = []


@app.route('/')
def home():
    books = BOOKS.query.all()

    return render_template('index.html', books=all_books)


@app.route('/add', methods=["POST", "GET"])
def add_book():
    if request.method == "POST":
        data = request.form
        title = data["name"]
        author = data["author"]
        rating = data["rating"]

        new_book = {
            "title": data["name"],
            "author": data["author"],
            "rating": data["rating"]
        }
        all_books.append(new_book)

        with app.app_context():
            enter_books_data = BOOKS(name=title, author=author, rating=rating)
            db.session.add(enter_books_data)
            db.session.commit()

        return redirect(url_for('home'))

    return render_template('add_book.html')


@app.route('/delete/<string:name>', methods="GET")
def delete_book(name):
    delete_book = BOOKS.query.filter_by(name=name).first()

    if delete_book:
        db.session.delete(delete_book)
        db.session.commit()
        flash(f'the book {name} is deleted succesfully')

    else:
        flash(f'Book with the name "{name}" not found!', 'danger')

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
