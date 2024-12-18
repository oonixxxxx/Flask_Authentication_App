from flask import Flask
from flask_wtf import CSRFProtect

# Создаем экземпляр Flask-приложения
app = Flask(__name__)

# Загружаем конфигурацию из файла config.py
app.config.from_object('config.Config')

# Инициализация CSRF защиты
csrf = CSRFProtect(app)

# Импортируем маршруты, чтобы они были зарегистрированы в приложении
from app import routes