from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)


try:
    product: Product = Product(name="Laptop", price=5000000, quantity=0)
except Exception as e:
    print(e)


# This code will Raise Validation Error for quantity parameter.
# same for name if Name = "PC" and price if price = -100
