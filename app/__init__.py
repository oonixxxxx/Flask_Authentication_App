from flask import Flask

# Создаем экземпляр Flask-приложения
app = Flask(__name__)

# Загружаем конфигурацию из файла config.py
app.config.from_object('config.Config')

# Импортируем маршруты, чтобы они были зарегистрированы в приложении
from app import routes