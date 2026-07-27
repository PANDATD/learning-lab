from python_fundamentals.exercises.pricing import (
    calculate_discounted_price,
)


def test_discounted_price() -> None:
    result: float = calculate_discounted_price(
        price=100, quantity=2, discount_percentage=10
    )

    assert result == 180.0
