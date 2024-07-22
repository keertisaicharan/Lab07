from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import User
from utils import check_password
import bcrypt

@app.route('/')
def home():
    return redirect(url_for('signin'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('signup'))
        
        password_errors = check_password(password)
        if password_errors:
            for error in password_errors:
                flash(error)
            return redirect(url_for('signup'))

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists')
            return redirect(url_for('signup'))
        
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully')
        return redirect(url_for('thankyou'))

    return render_template('templates/signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password):
            flash('Please check your login details and try again.')
            return redirect(url_for('signin'))

        flash('Logged in successfully')
        return redirect(url_for('success'))

    return render_template('templates/signin.html')

@app.route('/success')
def success():
    return render_template('templates/secretPage.html')

@app.route('/thankyou')
def thankyou():
    return render_template('templates/thankyou.html')