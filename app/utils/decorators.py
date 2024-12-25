from functools import wraps
from app.utils.exceptions import BaseAPIException
from flask import jsonify

def handle_exceptions(f):
    """
    Декоратор для обработки исключений в API
    
    Автоматически обрабатывает все исключения и возвращает
    соответствующий HTTP-ответ с сообщением об ошибке
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except BaseAPIException as e:
            # Обработка известных исключений API
            return jsonify(error=str(e)), e.status_code
        except Exception as e:
            # Обработка непредвиденных исключений
            return jsonify(error="Internal server error"), 500
    return decorated 