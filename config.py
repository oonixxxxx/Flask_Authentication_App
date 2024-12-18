import os

# Класс конфигурации приложения
class Config:
    # Секретный ключ для защиты сессий и данных
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    # Здесь можно добавить другие параметры конфигурации 