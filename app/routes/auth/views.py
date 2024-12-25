from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from app.models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash('Успешный вход')
            return redirect(url_for('main.index'))
        
        flash('Неверный email или пароль')
    return render_template('auth/login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect(url_for('main.index'))
    return render_template('auth/signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index')) 