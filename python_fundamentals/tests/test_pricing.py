from python_fundamentals.exercises.pricing import (
    calculate_discounted_price,
)


def test_discounted_price():
    result = calculate_discounted_price(100, 2, 10)

    assert result == 180.0
