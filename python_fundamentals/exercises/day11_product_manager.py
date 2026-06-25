#!/usr/bin/env python3.12
class Product:
    """
    This class represents Product

    Args:
        name: str
        price: float
        quantity: int
    """

    tax_rate: float = 0.18  # class attribute

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self) -> None:
        """
        This method prints the information of product on console.
        """
        print(
            f"""Product Name: {self.name}\n
            Price: {self.price}\n
            Quantity: {self.quantity}\n""",
            end="\n",
        )

    def total_value(self) -> float:
        """
        This method returns the total value of product
        Returns:
            self.price * self.quantity
        """
        return self.price * self.quantity

    def apply_discount(self, percentage: float) -> None:
        """

        This method apply discount and update the price.
        This also a state chaning method

        Args:
            percentage: float
            Returns:
                None

        """
        self.percentage = percentage
        self.price = self.price - (self.price * self.percentage / 100)

    def discounted_price(self, percentage: float) -> float:
        """
        This method returns the discounted price
        Args:
            percentage: float
            Returns:
                self.percentage: float
        """
        self.percentage = percentage
        return self.price - (self.price * self.percentage / 100)


if __name__ == "__main__":
    mobile: Product = Product(name="Motorola G35", price=12_000, quantity=2)

    laptop: Product = Product(
        name="Asus a17 TUF gameing laptop", price=1_20_000, quantity=1
    )

    mobile.display()
    mobile.total_value()
    discounted_price = mobile.discounted_price(percentage=10)
    print(discounted_price)
    print(mobile.price)
    mobile.apply_discount(percentage=10)
    print(mobile.price)
    mobile.tax_rate

    laptop.display()
    laptop.total_value()
    discounted_price = laptop.discounted_price(percentage=10)
    print(discounted_price)
    print(laptop.price)
    laptop.apply_discount(percentage=10)
    print(laptop.price)
    laptop.tax_rate
