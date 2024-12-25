<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ONIX HUB - Documentation</title>
    <style>
        :root {
            --primary: #2563eb;
            --background: #0f172a;
            --surface: #1e293b;
            --text: #e2e8f0;
            --text-secondary: #94a3b8;
        }

        body {
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background: var(--background);
            color: var(--text);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .header {
            text-align: center;
            padding: 4rem 0;
            background: var(--surface);
            margin-bottom: 2rem;
        }

        .header h1 {
            font-size: 3rem;
            margin: 0;
            background: linear-gradient(to right, var(--primary), #60a5fa);
            -webkit-background-clip: text;
            color: transparent;
        }

        .badges {
            display: flex;
            gap: 1rem;
            justify-content: center;
            margin: 1rem 0;
        }

        .badge {
            padding: 0.5rem 1rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 500;
            background: var(--surface);
            color: var(--text);
            text-decoration: none;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }

        .feature-card {
            background: var(--surface);
            padding: 2rem;
            border-radius: 1rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .feature-card h3 {
            margin-top: 0;
            color: var(--primary);
        }

        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 2rem;
            justify-content: center;
            margin: 2rem 0;
        }

        .tech-item {
            text-align: center;
            width: 96px;
        }

        .tech-item img {
            width: 48px;
            height: 48px;
        }

        .section {
            margin: 4rem 0;
        }

        .section h2 {
            color: var(--primary);
            margin-bottom: 1.5rem;
        }

        code {
            display: block;
            background: var(--surface);
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            margin: 1rem 0;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }

        th, td {
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .contact-links {
            display: flex;
            gap: 1rem;
            justify-content: center;
            margin: 2rem 0;
        }

        .contact-link {
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            background: var(--surface);
            color: var(--text);
            text-decoration: none;
            transition: transform 0.2s;
        }

        .contact-link:hover {
            transform: translateY(-2px);
        }

        footer {
            text-align: center;
            padding: 2rem;
            background: var(--surface);
            margin-top: 4rem;
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <h1>🛍️ ONIX HUB</h1>
            <p>Современная платформа электронной коммерции на Flask</p>
            <div class="badges">
                <span class="badge">Python 3.9+</span>
                <span class="badge">MIT License</span>
                <span class="badge">Tests Passing</span>
                <span class="badge">95% Coverage</span>
            </div>
        </div>
    </header>

    <main class="container">
        <section class="section">
            <h2>✨ Особенности</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <h3>🛍️ Магазин</h3>
                    <ul>
                        <li>Каталог продуктов</li>
                        <li>Категории товаров</li>
                        <li>Корзина покупок</li>
                        <li>Оформление заказов</li>
                    </ul>
                </div>
                <div class="feature-card">
                    <h3>🔐 Безопасность</h3>
                    <ul>
                        <li>JWT авторизация</li>
                        <li>Защита от CSRF</li>
                        <li>Rate limiting</li>
                        <li>Безопасные заголовки</li>
                    </ul>
                </div>
                <div class="feature-card">
                    <h3>⚡ Производительность</h3>
                    <ul>
                        <li>Redis кэширование</li>
                        <li>Celery для задач</li>
                        <li>Nginx как прокси</li>
                        <li>Docker контейнеры</li>
                    </ul>
                </div>
                <div class="feature-card">
                    <h3>🔧 Разработка</h3>
                    <ul>
                        <li>Чистая архитектура</li>
                        <li>Type hints</li>
                        <li>Автотесты</li>
                        <li>CI/CD pipeline</li>
                    </ul>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>🛠 Технологии</h2>
            <div class="tech-stack">
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=python" alt="Python">
                    <p>Python</p>
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=flask" alt="Flask">
                    <p>Flask</p>
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=postgres" alt="PostgreSQL">
                    <p>PostgreSQL</p>
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=redis" alt="Redis">
                    <p>Redis</p>
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=docker" alt="Docker">
                    <p>Docker</p>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>📝 API Документация</h2>
            <table>
                <thead>
                    <tr>
                        <th>Метод</th>
                        <th>Endpoint</th>
                        <th>Описание</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>GET</td>
                        <td>/api/products</td>
                        <td>Список продуктов</td>
                    </tr>
                    <tr>
                        <td>GET</td>
                        <td>/api/products/{id}</td>
                        <td>Детали продукта</td>
                    </tr>
                    <tr>
                        <td>POST</td>
                        <td>/api/products</td>
                        <td>Создать продукт</td>
                    </tr>
                    <tr>
                        <td>PUT</td>
                        <td>/api/products/{id}</td>
                        <td>Обновить продукт</td>
                    </tr>
                    <tr>
                        <td>DELETE</td>
                        <td>/api/products/{id}</td>
                        <td>Удалить продукт</td>
                    </tr>
                </tbody>
            </table>
        </section>

        <section class="section">
            <h2>📦 Установка</h2>
            <code>
# Клонирование репозитория
git clone https://github.com/your-username/onixhub.git
cd onixhub

# Запуск через Docker
docker-compose up -d
            </code>
        </section>

        <section class="section">
            <h2>📞 Контакты</h2>
            <div class="contact-links">
                <a href="https://t.me/onixexe" class="contact-link">Telegram</a>
                <a href="https://github.com/oonixxxxx" class="contact-link">GitHub</a>
            </div>
        </section>

        <section class="section">
            <h2>📁 Структура проекта</h2>
            <code>
project/
├── app/
│   ├── __init__.py           # Инициализация Flask приложения
│   ├── config.py             # Конфигурация приложения
│   ├── models/               # Модели данных
│   │   ├── __init__.py
│   │   ├── mixins.py        # Миксины для моделей (TimestampMixin, SoftDeleteMixin)
│   │   └── product.py       # Модель Product
│   ├── services/            # Бизнес-логика
│   │   ├── __init__.py
│   │   └── product_service.py # Сервис для работы с продуктами
│   ├── static/              # Статические файлы
│   │   ├── css/
│   │   │   └── style.css    # Основные стили
│   │   ├── js/
│   │   │   └── jquery.js    # JavaScript библиотеки
│   │   └── img/            # Изображения
│   ├── templates/           # Шаблоны
│   │   ├── base.html       # Базовый шаблон
│   │   ├── components/     # Компоненты
│   │   │   ├── header.html
│   │   │   └── footer.html
│   │   └── pages/         # Страницы
│   │       └── index.html
│   └── utils/             # Утилиты
│       ├── decorators.py  # Декораторы для API
│       └── exceptions.py  # Обработчики ошибок
├── docker/
│   ├── Dockerfile        # Конфигурация Docker
│   └── docker-compose.yml # Оркестрация контейнеров
├── tests/               # Тесты
├── .env                # Переменные окружения
└── requirements.txt    # Зависимости проекта
            </code>
        </section>

        <section class="section">
            <h2>🔧 Конфигурация</h2>
            <div class="feature-card">
                <h3>Переменные окружения (.env)</h3>
                <code>
# Основные настройки
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret

# База данных
DATABASE_URL=postgresql://user:password@localhost/dbname
DEV_DATABASE_URL=postgresql://user:password@localhost/dev_dbname

# Redis
REDIS_URL=redis://localhost:6379/0

# Мониторинг
SENTRY_DSN=your-sentry-dsn
                </code>
            </div>
        </section>

        <section class="section">
            <h2>🔄 CI/CD Pipeline</h2>
            <div class="feature-card">
                <h3>GitHub Actions Workflow</h3>
                <code>
name: CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:13
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
    - name: Run tests
      run: pytest --cov=app tests/

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    steps:
    - name: Deploy to production
      uses: appleboy/ssh-action@master
                </code>
            </div>
        </section>

        <section class="section">
            <h2>🐳 Docker</h2>
            <div class="feature-card">
                <h3>Сервисы</h3>
                <ul>
                    <li>Web (Flask application)</li>
                    <li>PostgreSQL (База данных)</li>
                    <li>Redis (Кэширование)</li>
                    <li>Celery (Асинхронные задачи)</li>
                    <li>Nginx (Обратный прокси)</li>
                </ul>
            </div>
        </section>

        <section class="section">
            <h2>📊 Мониторинг и логирование</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <h3>Healthcheck</h3>
                    <p>Endpoint: <code>/health</code></p>
                    <p>Проверяет:</p>
                    <ul>
                        <li>Доступность базы данных</li>
                        <li>Подключение к Redis</li>
                        <li>Состояние Celery</li>
                    </ul>
                </div>
                <div class="feature-card">
                    <h3>Логирование</h3>
                    <ul>
                        <li>Структурированные JSON логи</li>
                        <li>Ротация логов</li>
                        <li>Различные уровни логирования</li>
                    </ul>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>🔒 Безопасность</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <h3>Аутентификация</h3>
                    <ul>
                        <li>JWT токены</li>
                        <li>Защита от брутфорса</li>
                        <li>Безопасное хранение паролей</li>
                    </ul>
                </div>
                <div class="feature-card">
                    <h3>Защита</h3>
                    <ul>
                        <li>CSRF токены</li>
                        <li>Rate limiting</li>
                        <li>Secure headers</li>
                        <li>SQL injection protection</li>
                    </ul>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>🚀 Развертывание</h2>
            <div class="feature-card">
                <h3>Production</h3>
                <code>
# Обновление до последней версии
git pull origin main

# Сборка и запуск контейнеров
docker-compose -f docker-compose.prod.yml up -d --build

# Применение миграций
docker-compose exec web flask db upgrade
                </code>
            </div>
        </section>

    </main>

    <footer>
        <p>Made with ❤️ by ONIX</p>
    </footer>
</body>
</html> 