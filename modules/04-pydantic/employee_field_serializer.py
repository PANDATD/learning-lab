from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, field_serializer


class Employee(BaseModel):
    name: str
    salary: Decimal
    joining_date: date

    @field_serializer("salary")
    def salary_in_dollars(self, salary: Decimal) -> str:
        return f"${salary}"

    @field_serializer("joining_date")
    def format_date(self, date: datetime) -> str:
        return date.strftime("%d %b %Y")


emp1: Employee = Employee(
    name="Tejas Dixit",
    salary=Decimal(25000),
    joining_date=date(year=2024, month=1, day=29),
)

print(emp1.model_dump())
