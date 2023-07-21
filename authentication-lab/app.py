from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
    "apiKey": "AIzaSyDIoigRxqoG3yF1XhSEfnxnne1v3Yk4NLM",
    "authDomain": "ayoubtheg-bbc44.firebaseapp.com",
    "projectId": "ayoubtheg-bbc44",
    "storageBucket": "ayoubtheg-bbc44.appspot.com",
    "messagingSenderId": "981860393869",
    "appId": "1:981860393869:web:4e354995d6a8783ae193c4",
    "measurementId": "G-WGCERY71N7",
    "databaseURL": ""
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")




if __name__ == '__main__':
    app.run(debug=True)