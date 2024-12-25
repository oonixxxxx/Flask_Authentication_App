FROM python:3.9-slim

WORKDIR /app

# Установка зависимостей для разработки
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest pytest-cov

# Копирование кода приложения
COPY . .

# Команда по умолчанию для продакшена
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"] 