import pytest

from python_fundamentals.exercises.inventory import Product, validate_product


def test_invalid_product():
    with pytest.raises(ValueError):
        validate_product(
            Product(
                name="laptop",
                price=-100,
                quantity=1,
            )
        )
