from functools import wraps
from app.utils.exceptions import BaseAPIException
from flask import jsonify, abort
from flask_login import current_user

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

def admin_required(f):
    """Декоратор для проверки прав администратора"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function 