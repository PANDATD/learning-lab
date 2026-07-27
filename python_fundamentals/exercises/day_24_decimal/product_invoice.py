from decimal import Decimal

from pydantic import BaseModel, Field, computed_field


class Product(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    price: Decimal
    quantity: int

    @computed_field
    def subtotal(self) -> Decimal:
        return self.price * self.quantity


class Invoice(BaseModel):
    invoice_id: str
    customer_name: str = Field(min_length=3, max_length=20)
    products: list[Product]
    gst_percentage: Decimal

    @computed_field
    def subtotal_total(self) -> Decimal:
        total: Decimal = Decimal("0")
        for product in self.products:
            total += product.subtotal
        return total

    @computed_field
    def grand_total(self) -> Decimal:
        subtotal: Decimal = self.subtotal_total
        gst_amount = subtotal * (self.gst_percentage / 100)
        return Decimal(subtotal + gst_amount)


p1: Product = Product(name="Sugar", price=Decimal("20.00"), quantity=1)
p2: Product = Product(name="Oil", price=Decimal("120.00"), quantity=2)

invoice: Invoice = Invoice(
    invoice_id="123",
    customer_name="Tejas Dixit",
    products=[p1, p2],
    gst_percentage=Decimal("18"),
)

print(invoice.model_dump())
