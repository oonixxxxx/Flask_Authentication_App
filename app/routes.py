from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app import app
import sqlite3
from functools import wraps

# Декоратор для проверки авторизации пользователя
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Проверяем, есть ли пользователь в сессии
        if 'user_id' not in session:
            flash('Пожалуйста, войдите в систему')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Маршрут для входа в систему
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Подключаемся к базе данных и проверяем пользователя
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        user = c.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()
        
        # Проверяем пароль и устанавливаем сессию
        if user and check_password_hash(user[3], password):
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            flash('Вы успешно вошли в систему')
            return redirect(url_for('index'))
        
        flash('Неверный email или пароль')
    return render_template('login.html')

# Новый маршрут для страницы администратора
@app.route('/admin')
def admin_menu():
    return render_template('admin_menu.html')

# Маршрут для регистрации нового пользователя
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        
        # Проверяем совпадение паролей
        if password != confirm_password:
            flash('Пароли не совпадают')
            return render_template('signup.html')
        
        # Хешируем пароль для безопасности
        hashed_password = generate_password_hash(password)
        
        try:
            # Добавляем нового пользователя в базу данных
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)',
                     (name, email, hashed_password))
            conn.commit()
            conn.close()
            
            flash('Регистрация успешна! Теперь вы можете войти')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Email уже зарегистрирован')
        except Exception as e:
            flash('Произошла ошибка при регистрации')
            print(e)
    
    return render_template('signup.html')

# Маршрут для выхода из системы
@app.route('/logout')
def logout():
    # Очищаем сессию пользователя
    session.clear()
    flash('Вы вышли из системы')
    return redirect(url_for('index'))

# Главная страница приложения
@app.route('/')
def index():
    # Получаем имя пользователя из сессии
    user_name = session.get('user_name')
    return render_template('index.html', user_name=user_name)

# Функция для создания таблицы пользователей в базе данных
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         email TEXT UNIQUE NOT NULL,
         password TEXT NOT NULL)
    ''')
    conn.commit()
    conn.close()

# Инициализация базы данных при запуске приложения
init_db() 