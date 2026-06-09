def calculate_discounted_price(
    price: float,
    quantity: int,
    discount_percentage: float,
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

    if price <= 0:
        raise ValueError("Price must be greater than 0")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if discount_percentage < 0:
        raise ValueError(
            "Discount percentage cannot be negative"
        )

    if discount_percentage > 100:
        raise ValueError(
            "Discount percentage cannot exceed 100"
        )

    discounted_price = price * (
        1 - discount_percentage / 100
    )

    return discounted_price * quantity
