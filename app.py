from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = '1234'

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
# all_books = []


@app.route('/')
def home():
    books = BOOKS.query.all()

    return render_template('index.html', books=books)


@app.route('/add', methods=["POST", "GET"])
def add_book():
    if request.method == "POST":
        data = request.form
        title = data["name"]
        author = data["author"]
        rating = data["rating"]

        try:
            with app.app_context():
                enter_books_data = BOOKS(name=title, author=author, rating=rating)
                db.session.add(enter_books_data)
                db.session.commit()
                flash('Book added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding the book: {str(e)}', 'danger')

        return redirect(url_for('home'))

    return render_template('add_book.html')


@app.route('/delete/<string:title>', methods=["GET"])
def delete_book(title):
    book_to_delete = BOOKS.query.filter_by(name=title).first()

    if book_to_delete:
        try:
            db.session.delete(book_to_delete)
            db.session.commit()
            flash(f'The book "{title}" has been deleted successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error deleting the book "{title}": {str(e)}', 'danger')
    else:
        flash(f'Book with the name "{title}" not found!', 'danger')

    return redirect(url_for("home"))


@app.route('/update/<string:title>', methods=["GET", "POST"])
def update_book(title):
    book_to_update = BOOKS.query.filter_by(name=title).first()

    if request.method == "POST":
        data = request.form


if __name__ == '__main__':
    app.run(debug=True)
