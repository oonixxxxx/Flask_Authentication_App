class BaseAPIException(Exception):
    """Базовый класс для исключений API"""
    status_code = 500
    
    def __init__(self, message=None, status_code=None):
        super().__init__(message)
        if status_code is not None:
            self.status_code = status_code
        self.message = message

class ProductNotFoundError(BaseAPIException):
    """Исключение для случая, когда продукт не найден"""
    def __init__(self, message="Product not found"):
        super().__init__(message, status_code=404)

class ValidationError(BaseAPIException):
    """Исключение для ошибок валидации"""
    def __init__(self, message="Validation error"):
        super().__init__(message, status_code=400)

class AuthenticationError(BaseAPIException):
    """Исключение для ошибок аутентификации"""
    def __init__(self, message="Authentication failed"):
        super().__init__(message, status_code=401)

class AuthorizationError(BaseAPIException):
    """Исключение для ошибо�� авторизации"""
    def __init__(self, message="Not authorized"):
        super().__init__(message, status_code=403) 