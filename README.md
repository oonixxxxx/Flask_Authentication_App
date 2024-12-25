<div align="center">
  <img src="app/static/img/logo.png" alt="ONIX HUB Logo" width="200"/>

  # 🛍️ ONIX HUB

  *Современная платформа электронной коммерции на Flask*

  [![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
  [![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)
  [![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg?style=for-the-badge&logo=github-actions&logoColor=white)](tests)
  [![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen.svg?style=for-the-badge&logo=codecov&logoColor=white)](coverage)
</div>

---

<p align="center">
  <a href="#особенности">Особенности</a> •
  <a href="#технологии">Технологии</a> •
  <a href="#установка">Установка</a> •
  <a href="#api-документация">API</a> •
  <a href="#развертывание">Развертывание</a>
</p>

---

## 📚 О проекте
> ONIX HUB - это современная платформа электронной коммерции, построенная с использованием Flask и современных технологий веб-разработки. Проект реализует полноценный интернет-магазин с расширенной функциональностью.

## ✨ Особенности
<table>
  <tr>
    <td>
      <h3>🛍️ Магазин</h3>
      <ul>
        <li>📋 Каталог продуктов</li>
        <li>🏷️ Категории товаров</li>
        <li>🛒 Корзина покупок</li>
        <li>📦 Оформление заказов</li>
      </ul>
    </td>
    <td>
      <h3>🔐 Безопасность</h3>
      <ul>
        <li>🔑 JWT авторизация</li>
        <li>🛡️ Защита от CSRF</li>
        <li>⚡ Rate limiting</li>
        <li>🔒 Безопасные заголовки</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <h3>⚡ Производительность</h3>
      <ul>
        <li>💾 Redis кэширование</li>
        <li>📊 Celery для задач</li>
        <li>🚀 Nginx как прокси</li>
        <li>🐳 Docker контейнеры</li>
      </ul>
    </td>
    <td>
      <h3>🔧 Разработка</h3>
      <ul>
        <li>📐 Чистая архитектура</li>
        <li>📝 Type hints</li>
        <li>🧪 Автотесты</li>
        <li>🔄 CI/CD pipeline</li>
      </ul>
    </td>
  </tr>
</table>

## 🛠 Технологии
<div align="center">
  <p>
    <a href="https://www.python.org">
      <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    </a>
    <a href="https://flask.palletsprojects.com">
      <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
    </a>
    <a href="https://www.postgresql.org">
      <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
    </a>
  </p>
  <p>
    <a href="https://redis.io">
      <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis" />
    </a>
    <a href="https://www.docker.com">
      <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
    </a>
    <a href="https://nginx.org">
      <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="Nginx" />
    </a>
  </p>
</div>
## 📁 Структура проекта 

<div align="center">
<pre class="project-structure">
project/
├── app/
│   ├── __init__.py           # Инициализация Flask приложения
│   ├── config.py             # Конфигурация приложения
│   ├── models/               # Модели данных
│   │   ├── mixins.py        # Миксины для моделей
│   │   └── product.py       # Модель Product
│   ├── services/            # Бизнес-логика
│   │   └── product_service.py
│   ├── static/              # Статические файлы
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   ├── templates/           # Шаблоны
│   │   ├── base.html
│   │   ├── components/
│   │   └── pages/
│   └── utils/              # Утилиты
│       ├── decorators.py
│       └── exceptions.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── tests/                  # Тесты
├── .env                    # Переменные окружения
└── requirements.txt        # Зависимости
</pre>
</div>

## 📦 Установка

### Через Docker (рекомендуется)

Клонирование репозитория
git clone https://github.com/your-username/onixhub.git
cd onixhub
Настройка окружения
cp .env.example .env
Запуск через Docker
docker-compose up -d

### Локальная установка

Создание виртуального окружения
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
Установка зависимостей
pip install -r requirements.txt
Настройка базы данных
flask db upgrade
Запуск
flask run


## 📝 API Документация

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | /api/products | Список продуктов |
| GET | /api/products/{id} | Детали продукта |
| POST | /api/products | Создать продукт |
| PUT | /api/products/{id} | Обновить продукт |
| DELETE | /api/products/{id} | Удалить продукт |

## 🔧 Конфигурация

Пример `.env` файла:

env
Основные настройки
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
База данных
DATABASE_URL=postgresql://user:password@localhost/dbname
DEV_DATABASE_URL=postgresql://user:password@localhost/dev_dbname
Redis
REDIS_URL=redis://localhost:6379/0
Мониторинг
SENTRY_DSN=your-sentry-dsn


## 🧪 Тестирование

bash
Запуск тестов
pytest
С отчётом о покрытии
pytest --cov=app tests/


## 📈 Мониторинг

### Healthcheck
- Endpoint: `/health`
- Проверяет:
  - Доступность базы данных
  - Подключение к Redis
  - Состояние Celery

### Логирование
- Структурированные JSON логи
- Ротация логов
- Различные уровни логирования
- Интеграция с Sentry

## 🚀 Развертывание

### Production

bash
Обновление до последней версии
git pull origin main
Сборка и запуск контейнеров
docker-compose -f docker-compose.prod.yml up -d --build
Применение миграций
docker-compose exec web flask db upgrade


### CI/CD Pipeline

- **Тестирование**:
  - Запуск unit-тестов
  - Проверка типов
  - Анализ кода
- **Развертывание**:
  - Автоматическая сборка Docker образо��
  - Развертывание в production
  - Мониторинг развертывания

## 📞 Контакты

- Telegram: [@onixexe](https://t.me/onixexe)
- GitHub: [@oonixxxxx](https://github.com/oonixxxxx)

## 📄 Лицензия

MIT License

Copyright (c) 2024 ONIX HUB

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

---

<div align="center">
Made with ❤️ by ONIX
</div>