from dataclasses import asdict, dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int



mobile = Product(
    name="Motorola G35",
    price=12_000,
    quantity=2
)

# Here i can access the product info using object.attribute

print(
    mobile.name,
    mobile.price,
    mobile.quantity
)


# This will prints the product object into dictitonry representation.
print(asdict(mobile))

# Lets we can modify the price of product
mobile.price = 12_500.00
print(mobile)


"""
    we can make our dataclass immutable using the frozen=True
    if we pass the frozen to decorator so the class is immutable
"""
