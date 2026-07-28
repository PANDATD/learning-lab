from datetime import date, datetime
from decimal import Decimal
from enum import StrEnum
from pprint import pprint

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    computed_field,
    field_serializer,
    field_validator,
)


class AllowedState(StrEnum):
    MAHARASHTRA = "MAHARASHTRA"
    UP = "UTTARPRADESH"
    MP = "MADHYAPRADESH"
    KARNATAKA = "KARNATAKA"


class Address(BaseModel):
    city: str = Field(min_length=3, max_length=20)
    pincode: str = Field(min_length=6, max_length=6)
    state: AllowedState


class AllowedDepartment(StrEnum):
    CONTENT = "CONTENT"
    ADMIN = "ADMIN"
    TECHNICAL = "TECHNICAL"
    DATA = "DATA"


class Employee(BaseModel):
    emp_name: str = Field(min_length=3, max_length=30)
    email: EmailStr | None = None
    department: AllowedDepartment
    salary: Decimal
    address: Address
    joining_date: date
    created_at: datetime

    @field_validator("emp_name")
    def _validate_format_emp_name(cls, emp_name: str) -> str:
        words = emp_name.strip().split()
        emp_name = " ".join(words).title()
        for char in emp_name:
            if not (char.isalpha() or char.isspace() or char in ("-", "'")):
                raise ValueError(
                    "Employee name must only contain letters, \
                    spaces, hyphens, or apostrophes."
                )
        return emp_name

    @field_serializer("salary")
    def salary_in_dollars(self, salary: Decimal) -> str:
        return f"${salary}"

    @computed_field
    def annual_salary(self) -> Decimal:
        return 12 * self.salary

    @field_serializer("annual_salary")
    def _format_annual_salary(self, annual_salary: Decimal) -> str:
        return f"${annual_salary}"

    @field_serializer("joining_date")
    def format_date_content_dept(self, joining_date: date) -> str:
        return str(joining_date.strftime(format="%d %b %Y"))


class Company(BaseModel):
    address: Address
    employees: list[Employee]


tejas_dixit: Employee = Employee(
    emp_name="  teJaS   diXit  ",
    email="tejasdixit17@zohomail.in",
    department=AllowedDepartment.CONTENT,
    salary=Decimal("25000"),
    joining_date=date(year=2024, month=1, day=29),
    created_at=datetime(year=2024, month=1, day=28, hour=20, minute=12),
    address=Address(city="Pune", pincode="411028", state=AllowedState.MAHARASHTRA),
)


vignesh_gawali: Employee = Employee(
    emp_name="  Vignesh  Gawali   ",
    department=AllowedDepartment.TECHNICAL,
    salary=Decimal("25000"),
    joining_date=date(year=2024, month=1, day=29),
    created_at=datetime(year=2024, month=1, day=28, hour=20, minute=30, second=56),
    address=Address(city="Pune", pincode="411005", state=AllowedState.MAHARASHTRA),
)


company_address: Address = Address(
    city="Bengluru", pincode="311098", state=AllowedState.KARNATAKA
)


tcs: Company = Company(address=company_address, employees=[tejas_dixit, vignesh_gawali])

pprint(tcs.model_dump())
