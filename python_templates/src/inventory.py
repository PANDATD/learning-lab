"""

Assignment: Product Inventory Manager
Problem Statement
Create a simple inventory system that stores products and calculates inventory value.

"""

from contextlib import contextmanager
from dataclasses import asdict, dataclass


@dataclass
class Product:
    name: str
    price: float | int
    quantity: int


"""

I choose the dataclass inseted of simple dicitionay,
beacuse i have to avoid the misspelled key names and by defult it creates
constructor __init__ for me.

"""


def validate_product(product: Product) -> None:
    """

    - validate_product takes product as an argument type of Product
    and apply validation rules.

    - must require name, price, quantity

    Args:
        name : str
        price: float | int
        quantity: int
    Returns:
        None
    """

    if not product.name:
        raise ValueError("Product name is required")

    if not isinstance(product.price, (float, int)):
        raise TypeError(f"price {product.price} of product must be int or float")

    if product.price <= 0 or not product.price:
        raise ValueError("Price is required and product.price must be gretter than 0")

    if not product.quantity:
        raise ValueError("Prodcut Quantity is required.")

    if not isinstance(product.quantity, (float, int)):
        raise TypeError(f"Qty: {product.quantity} must be Numaric and gretter than 0")

    return None


def calculate_inventory_value(products: list[Product]) -> float:
    """
    Calculates the Total value of products in list.
    Args:
        products: list[Product]
    Returns:
        total: flat
    """
    total = 0
    for product in products:
        total += product.price * product.quantity
    return total


@contextmanager
def inventory_session():
    """Creating inventory session"""
    print("Opning inventory session\n")
    yield
    print("Closing inventory session\n")


def export_products(products: list[Product]) -> list[dict[str, object]]:
    """
    exports the products in dict format
    Args:
        products: list[Product]
    """
    products_list: list = []
    for product in products:
        products_list.append(asdict(product))
    return products_list


def main():

    with inventory_session():
        # product creation
        p1 = Product(name="Motorola G34 5G", price=20_000.96, quantity=1)
        p2 = Product(name="Motorola edage 40 neo 5G", price=40_808.86, quantity=2)

        # product validation
        validate_product(p1)
        validate_product(p2)

        products: list[Product] = [p1, p2]

        # export products to dict
        products_list = export_products(products)
        print(products_list)

        # calculate total inventory value
        total = calculate_inventory_value(products=products)
        print(f"Total value of all inventory: {total}\n")


if __name__ == "__main__":
    main()
