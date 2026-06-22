def calculate_discounted_price(
    price: int | float,
    quantity: int,
    discount_percentage: int | float,
) -> float:
    """
    Calculate the discounted total price.

    Args:
        price: Price of a single item.
        quantity: Number of units.
        discount_percentage: Discount percentage.

    Returns:
        Discounted total price.
    """

    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number")

    if not isinstance(quantity, int):
        raise TypeError("Quantity must be an integer")

    if isinstance(quantity, bool):
        raise TypeError("Quantity cannot be a boolean")

    if not isinstance(
        discount_percentage,
        (int, float),
    ):
        raise TypeError("Discount percentage must be a number")

    if price <= 0:
        raise ValueError("Price must be greater than 0")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if discount_percentage < 0:
        raise ValueError("Discount percentage cannot be negative")

    if discount_percentage > 100:
        raise ValueError("Discount percentage cannot exceed 100")

    discounted_price = price * (1 - discount_percentage / 100)

    return float(discounted_price * quantity)
