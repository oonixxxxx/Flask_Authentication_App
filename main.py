from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Замените на случайный секретный ключ

# Функция для создания таблицы пользователей
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

# Декоратор для проверки авторизации
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Пожалуйста, войдите в систему')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        user = c.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user[3], password):
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            flash('Вы успешно вошли в систему')
            return redirect(url_for('index'))
        
        flash('Неверный email или пароль')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        
        if password != confirm_password:
            flash('Пароли не совпадают')
            return render_template('signup.html')
        
        hashed_password = generate_password_hash(password)
        
        try:
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

@app.route('/logout')
def logout():
    session.clear()
    flash('Вы вышли из системы')
    return redirect(url_for('index'))

# Обновляем маршрут index для отображения информации о пользователе
@app.route('/')
def index():
    user_name = session.get('user_name')
    return render_template('index.html', user_name=user_name)

# Инициализация базы данных при запуске
init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)