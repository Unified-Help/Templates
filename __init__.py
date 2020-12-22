from flask import Flask, render_template, request, redirect, url_for, session
from Forms import CreateUserForm
import shelve, User

app = Flask(__name__)


@app.route("/")
def home():
    # return "Hello World!"
    return render_template('index.html')


if __name__ == "__main__":
    app.run()