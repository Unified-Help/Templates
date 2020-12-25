from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


@app.route("/")
def home():
    # return "Hello World!"
    return render_template('index.html')


@app.route("/donate")
def donate():
    return render_template('Donate.html')


@app.route("/forum")
def forum():
    return render_template('Forum.html')

@app.route("/faq")
def faq():
    return render_template('FAQ.html')


@app.route("/account")
def account():
    return render_template('Account.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)

