from flask import Flask, jsonify, request, session, redirect, url_for, render_template
from passlib.hash import pbkdf2_sha256
from app import db, dashboard
import uuid

class User:

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    user_id = user['_id']
    return redirect(url_for('dashboard', user=user_id))

  def signup(self):
    print(request.form)

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "category": request.form.get("category"),
      "first_name": request.form.get('first_name'),
      "last_name": request.form.get('last_name'),
      "matric_no": request.form.get('matric_no'),
      "email": request.form.get('email'),
      "phone_number": request.form.get('phone_number'),
      "current_level": request.form.get('current_level'),
      "password": request.form.get('password'),
      "confirm_password": request.form.get('confirm_password'),
    }

    # Check for existing email address
    if db['users'].find_one({ "email": user['email'] }):
      return render_template('signup.html', message='Email already in use!')
    if db['users'].find_one({'matric_no':user["matric_no"]}):
      return render_template('signup.html', message="Matric Number already in use!")
    if user["password"] == user['confirm_password']:
      # Encrypt the password
      user['password'] = pbkdf2_sha256.encrypt(user['password'])
      del user['confirm_password']
      if db.users.insert_one(user):
        return redirect(url_for('loginpage'))
    else:
      return render_template('signup.html', message="Password Mismatch!")

    return render_template('signup.html', message='Error! Sign Up failed')
  
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):

    user = db['users'].find_one({
      "email": request.form.get('email')
    })

    if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
      return self.start_session(user)
    
    return render_template('login.html', message='Invalid login details')