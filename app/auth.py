from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password1')
        cnfm_password = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            #flash('Email already exists', 'error')
            print('Email already exists')
        elif len(email) < 4:
            #flash("Email must be greater than 4 characters", category='error')
            print('Email must be greater than 4 characters')
        elif len(name) < 2:
            #flash("Name must be greater than 2 characters", category='error')
            print('Name must be greater than 2 characters')
        elif len(password) < 7:
            print('Password is too short')
            #flash("Password is too short", category='error')
        elif password != cnfm_password:
            #flash("Passwords do not match", category='error')
            print('Passwords do not match')
        else:
            new_user = User(email=email, full_name=name, hashed_password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()            
            #flash("Account created!", category='success')
            login_user(user=user, remember=True)
            return redirect(url_for('views.home'))

    return render_template('signup.html', user=current_user)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.hashed_password, password):
                #flash('Logged in successfully!', 'success')
                print('Logged in sucessfully')
                login_user(user=user, remember=True)
                return redirect(url_for('views.home'))
            else:
                #flash('Incorrect Password, Try again', 'error')
                print('Incorrect password')
        else:
            #flash('Email does not exist', 'error')
            print('Email does not exist')
    return render_template('login.html', user=current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))