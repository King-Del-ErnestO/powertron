from flask import Flask, render_template, url_for, session, redirect, request
from functools import wraps
from pymongo import MongoClient
from flask_cors import CORS
import cloudinary.uploader
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = b'bjbvjbovlbvjbvsbvlbvvblblvblvbbd'

cloudinary.config(
  cloud_name = "dhr6igdst",
  api_key = "578356959545128",
  api_secret = "GFvGFOvSVr0VfdeOMzos9BvU_Xc"
)


#Database
# mongo = MongoClient("mongodb://127.0.0.1:27017")
mongo = MongoClient("mongodb+srv://quickwork:quickwork@users.46fhmfp.mongodb.net/?retryWrites=true&w=majority")
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
    # print(user)
    # user_name = user['name']
    return render_template('dashboard/index.html', user=user)


@app.route('/signup/')
def signuppage():
    return render_template('signup.html')

@app.route('/login/')
def loginpage():
    return render_template('login.html')

@app.route('/profile/<user>')
def profile(user):
    print(user)
    user = db['users'].find_one({"_id": f'{user}'})
    print(user)
    return render_template("dashboard/profile.html", user=user)

@app.route('/profile_pic/<user>', methods=['POST'])
def uprofile(user):
    user = db['users'].find_one({"_id": f"{user}"})
    print(user)
    if "profile_image" in request.files:
        profile_image = request.files['profile_image']
        im_name = os.path.splitext(profile_image.filename)
        cloudinary.uploader.upload(profile_image, public_id=im_name[0])
        db['users'].update_one({"_id":user['_id']}, {"$set":{"profile_image_name":profile_image.filename}}, upsert=True)
        return redirect(url_for("profile", user=user['_id']))
    return render_template("dashboard/profile.html", user=user, message="Not successful!")


@app.route("/file/<filename>")
def file(filename):
    return cloudinary.utils.cloudinary_url(filename)[0]



port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

