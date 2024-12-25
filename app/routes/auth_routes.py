from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from . import auth
from app.models import User
from app import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Логика входа
        pass
    return render_template('auth/login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Логика регистрации
        pass
    return render_template('auth/signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index')) 