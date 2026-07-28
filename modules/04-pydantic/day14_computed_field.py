from pydantic import BaseModel, Field, computed_field, field_validator


class Employee(BaseModel):
    """This Model represents an employee"""

    first_name: str = Field(min_length=3, max_length=20)
    last_name: str = Field(min_length=2, max_length=20)
    monthly_salary: float = Field(gt=0)

    @field_validator("first_name")
    @classmethod
    def transform_first_name(cls, first_name: str) -> str:
        first_name = first_name.strip().title()
        return first_name

    @field_validator("last_name")
    @classmethod
    def transform_last_name(cls, last_name: str) -> str:
        last_name = last_name.strip().title()
        return last_name

    @computed_field
    def full_name(self) -> str:
        """This will return full name of an employee"""
        return f"{self.first_name} {self.last_name}"

    @computed_field
    def annual_salary(self) -> float:
        """This will return annual salary of an employee"""
        return self.monthly_salary * 12

    def change_first_name(self, first_nm: str) -> None:
        self.first_name = first_nm.strip().title()
        return None


class Product(BaseModel):
    """This Class Represents a Product"""

    name: str = Field(min_length=3, max_length=10)
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)
    discount_percentage: float = Field(gt=0, le=100)

    @field_validator("name")
    @classmethod
    def normalize_product_name(cls, name: str) -> str:
        name = name.strip().title()
        return name

    @computed_field
    def discount_amount(self) -> float:
        """Return the discount amount."""
        return self.price * (self.discount_percentage / 100)

    @computed_field
    def final_price(self) -> float:
        """Return the final price after discount."""
        return self.price - self.discount_amount  # type: ignore

    @computed_field
    def total_inventory_value(self) -> float:
        """Return the total inventory value."""
        return self.final_price * self.quantity  # type: ignore
