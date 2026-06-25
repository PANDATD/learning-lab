from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    quantity: int


if __name__ == "__main__":
    mobile: Product = Product(name="Motorola G35", price=50_0000.25, quantity=2)
    # Pydantic will convert this Numaric values surounded by quotes,
    print(mobile.model_dump())
    print(type(mobile.price))
    print(mobile.model_dump_json())
