from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '123'


@app.route('/', methods=["POST", "GET"])
def form_page():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        age = data["age"]
        return render_template("submitted_forms.html", name=name, email=email, age=age)
    return render_template("index.html")


@app.route('/submitted')
def submitted():
    return render_template("submitted_forms.html")


if __name__ == '__main__':
    app.run()
