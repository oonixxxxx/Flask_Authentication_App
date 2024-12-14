# Многопоточное Flask Приложение

Это демонстрационное Flask-приложение, показывающее работу с многопоточностью в Python. Приложение обрабатывает данные параллельно, используя ThreadPoolExecutor.

## Особенности

- Параллельная обработка данных с использованием ThreadPoolExecutor
- REST API для обработки данных
- Docker-контейнеризация
- Поддержка многопоточности

## Требования

- Python 3.9+
- Docker (опционально)

## Установка и запуск

### Локальный запуск

1. Создайте виртуальное окружение:

```
python -m venv venv
source venv/bin/activate # для Linux/Mac
venv\Scripts\activate # для Windows
```


2. Установите зависимости:

```
pip install -r requirements.txt
```

### Запуск через Docker

1. Соберите Docker-образ:

```
docker build -t flask-app .
```

2. Запустите контейнер:

```
docker run -p 5000:5000 flask-app
```

## API Endpoints

- `GET /` - главная страница приложения
- `POST /process` - endpoint для обработки данных

## Структура проекта

.
├── main.py # Основной файл приложения
├── requirements.txt # Зависимости проекта
├── Dockerfile # Конфигурация Docker
└── templates
└── index.html # Шаблон главной страницы

## Использование

После запуска приложение будет доступно по адресу http://localhost:5000

## Технологии

- Flask
- Threading
- ThreadPoolExecutor
- Docker
- Gunicorn