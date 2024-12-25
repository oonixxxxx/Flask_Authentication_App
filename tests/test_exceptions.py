import pytest
from app.utils.exceptions import ProductNotFoundError, ValidationError

def test_product_not_found_error():
    """Тест исключения ProductNotFoundError"""
    with pytest.raises(ProductNotFoundError) as exc:
        raise ProductNotFoundError("Product not found")
    assert str(exc.value) == "Product not found"

def test_validation_error():
    """Тест исключения ValidationError"""
    with pytest.raises(ValidationError) as exc:
        raise ValidationError("Invalid data")
    assert str(exc.value) == "Invalid data" 