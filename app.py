from flask import Flask, render_template, url_for, session, redirect
from functools import wraps
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = b'bjbvjbovlbvjbvsbvlbvvblblvblvbbd'

#Database
mongo = MongoClient("mongodb://127.0.0.1:27017")
db = mongo.triple_e

#Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap



#Routes

from user import models

@app.route('/user/signup', methods=['POST'])
def signup():
  return models.User().signup()

@app.route('/user/signout')
def signout():
  return models.User().signout()

@app.route('/user/login', methods=['POST'])
def login():
  return models.User().login()


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/dashboard/<user>')
@login_required
def dashboard(user):
    print(user)
    user = db['users'].find_one({"_id": f'{user}'})
    print(user)
    # user_name = user['name']
    return render_template('dashboard/index.html', user=user)


@app.route('/signup/')
def signuppage():
    return render_template('signup.html')

@app.route('/login/')
def loginpage():
    return render_template('login.html')



port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

