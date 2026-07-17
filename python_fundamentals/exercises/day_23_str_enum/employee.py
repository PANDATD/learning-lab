from enum import StrEnum

from pydantic import BaseModel, EmailStr, Field, field_validator

"""

Understand why StrEnum is used ?


Problem:

    - department : str = " HR"
    - department : str = "hr"
    - department : str = "Human Resource"

We know the Fixed Department and so we can resolve the same issue with StrEnum which
follow the consistancy for redundant but fixed values.

now StrEnum will gives JSON friendly ouput for department
but after serialization using `.model_dump_json()`

"""


class Department(StrEnum):
    ADMIN = "ADMIN"
    TECH = "TECH"
    DATA = "DATA"
    CONTENT = "CONTENT"


class Address(BaseModel):
    city: str | None = Field(
        default=None,
        min_length=3,
        max_length=10,
    )
    pincode: str | None = Field(default=None, min_length=6, max_length=6)


class Employee(BaseModel):
    """
    This class represent an Employee of a Company
    """

    emp_name: str = Field(min_length=3, max_length=60)
    emp_id: str = Field(min_length=7, max_length=20)
    email: EmailStr | None = None
    department: Department
    address: Address

    @field_validator("emp_name")
    @classmethod
    def transform_employee_name(cls, emp_name: str) -> str:
        """
        This method transforms emp_name and validates it
        removes whitespace and save employee name in title case
        """
        emp_name = emp_name.strip().title()

        if emp_name.isalpha():
            raise ValueError(
                f"Employee name has digits in it. \
                Employee name must be pure string and not contains digit. \
                you have entered {emp_name}"
            )
        return emp_name

    @field_validator("emp_id")
    @classmethod
    def transform_and_validate_employee_id(cls, emp_id: str) -> str:
        """
        This method helps to transforms and validate the employee id
        - Removes the whitespaces from emp_id
        - Capitalize the emp_id
        - Checks wether it strats with EMP-
        """
        emp_id = emp_id.strip().upper()

        if not emp_id.startswith("EMP-"):
            raise ValueError("Employee id must starts with EMP- ")

        if emp_id.isalnum():
            raise ValueError("Employee id must contain digits")

        return emp_id


class Company(BaseModel):
    """
    This Class represents company
    """

    company_name: str = Field(min_length=3, max_length=50)
    employees: list[Employee]

    @field_validator("company_name")
    @classmethod
    def transform_company_name(cls, company_name: str) -> str:
        company_name = company_name.strip().title()
        return company_name


tejas_dixit: Employee = Employee(
    emp_name="   tejas dixit   ",
    emp_id=" emp-108  ",
    email="tejasdixit17@gmail.com",
    address=Address(city="Pune", pincode="411028"),
    department=Department.TECH,
)

aniket_jagadale: Employee = Employee(
    emp_name=" aniket Jagadale",
    emp_id="EmP-107 ",
    department=Department.CONTENT,
    address=Address(),
)


media_vidya: Company = Company(
    company_name=" media VIdya pvt ltd", employees=[tejas_dixit, aniket_jagadale]
)


print(media_vidya.model_dump())  # prints normal model with python object for Department
print(media_vidya.model_dump_json())  # heare we can see department values pydantic
# serialize the output using model_dump_json()
# its API friendly and help when working with
# other languages.
