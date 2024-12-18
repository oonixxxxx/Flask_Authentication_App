from app import app

# Запуск приложения Flask
if __name__ == '__main__':
    # Приложение будет доступно на всех интерфейсах на порту 5000
    app.run(host='0.0.0.0', port=5000, debug=True) 