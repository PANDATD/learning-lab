"""
Assignment: Product Inventory Manager

Concepts Used:
- Dataclasses
- Type Hints
- Validation
- Context Managers
- asdict()
- Exception Handling

This module demonstrates a simple inventory management system
for storing products, validating product data, calculating
inventory value, and exporting products as dictionaries.
"""

from contextlib import contextmanager
from dataclasses import asdict, dataclass


@dataclass
class Product:
    """
    Represents a product in inventory.

    Attributes:
        name: Product name.
        price: Price of a single unit.
        quantity: Available stock quantity.
    """

    name: str
    price: float
    quantity: int


def validate_product(product: Product) -> None:
    """
    Validate a Product instance.

    Rules:
    - Name cannot be empty.
    - Price must be numeric and greater than zero.
    - Quantity must be an integer greater than zero.

    Args:
        product: Product instance to validate.

    Raises:
        TypeError:
            If price or quantity have invalid types.
        ValueError:
            If values violate business rules.
    """

    if not product.name.strip():
        raise ValueError("Product name is required.")

    if not isinstance(product.price, (int, float)):
        raise TypeError("Price must be numeric.")

    if product.price <= 0:
        raise ValueError("Price must be greater than zero.")

    if not isinstance(product.quantity, int):
        raise TypeError("Quantity must be an integer.")

    if product.quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")


def calculate_inventory_value(
    products: list[Product],
) -> float:
    """
    Calculate the total inventory value.

    Formula:
        product.price * product.quantity

    Args:
        products: List of Product objects.

    Returns:
        Total inventory value.
    """

    total = 0.0

    for product in products:
        total += product.price * product.quantity

    return total


@contextmanager
def inventory_session():
    """
    Simulate an inventory session.

    Demonstrates resource acquisition and cleanup
    using a context manager.
    """

    print("Opening inventory session...")

    try:
        yield
    finally:
        print("Closing inventory session...")


def export_products(
    products: list[Product],
) -> list[dict[str, object]]:
    """
    Convert Product objects into dictionaries.

    Args:
        products: List of Product instances.

    Returns:
        List of dictionaries.
    """

    exported_products: list[dict[str, object]] = []

    for product in products:
        exported_products.append(asdict(product))

    return exported_products


def main() -> None:
    """
    Execute inventory workflow.

    Steps:
    1. Create products.
    2. Validate products.
    3. Calculate inventory value.
    4. Export products.
    """

    with inventory_session():
        products = [
            Product(
                name="Motorola G34 5G",
                price=20_000.96,
                quantity=1,
            ),
            Product(
                name="Motorola Edge 40 Neo 5G",
                price=40_808.86,
                quantity=2,
            ),
        ]

        for product in products:
            validate_product(product)

        total_inventory_value = calculate_inventory_value(products)

        exported_products = export_products(products)

        print(exported_products)

        print(f"Total inventory value: {total_inventory_value}")


if __name__ == "__main__":
    main()
