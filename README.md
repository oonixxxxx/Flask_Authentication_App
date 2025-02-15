# Flask Authentication App

Это простое веб-приложение на Flask, которое демонстрирует базовую аутентификацию пользователей. Приложение позволяет пользователям регистрироваться, входить в систему и просматривать защищенные страницы.

## Особенности

- Регистрация новых пользователей.
- Вход в систему с использованием электронной почты и пароля.
- Защита маршрутов с помощью декоратора `@login_required`.
- Хэширование паролей с использованием `bcrypt`.
- Использование SQLite для хранения данных пользователей.

## Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/oonixxxxx/Flask_Authentication_App.git
   cd Flask_Authentication_App
   ```

2. **Создайте виртуальное окружение и активируйте его:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate      # Для Windows
   ```

3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте базу данных:**

   Приложение использует SQLite для хранения данных. Для инициализации базы данных выполните:

   ```bash
   python init_db.py
   ```

5. **Запустите приложение:**

   ```bash
   flask run
   ```

   Приложение будет доступно по адресу: `http://127.0.0.1:5000/`.

## Использование

- **Регистрация:** Перейдите по адресу `/register` и заполните форму.
- **Вход в систему:** Перейдите по адресу `/login` и введите свои учетные данные.
- **Защищенные страницы:** После успешного входа вы сможете получить доступ к защищенным страницам, например, `/dashboard`.

## Структура проекта

```
Flask_Authentication_App/
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   └── register.html
│   └── static/
│       └── styles.css
├── init_db.py
├── requirements.txt
└── README.md
```

## Зависимости

- Flask
- Flask-Login
- Flask-SQLAlchemy
- bcrypt

## Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](LICENSE).

## Автор

[oonixxxxx](https://github.com/oonixxxxx)
