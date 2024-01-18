from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

all_books=[]
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=["POST"])
def add_book():
    if request.method=="POST":
        data = request.form
    return render_template('add_book.html')


if __name__ == '__main__':
    app.run()
