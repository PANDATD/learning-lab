from enum import StrEnum

from pydantic import BaseModel, EmailStr, Field

# Company has Company Name and company has address and employees.


class Address(BaseModel):
    """This model represnts the Address"""

    city: str
    pincode: str = Field(min_length=6, max_length=6)
    state: str


class Employee(BaseModel):
    """This Model Represents the an Employee"""

    employee_id: str
    name: str = Field(max_length=20, min_length=0)
    email: EmailStr
    address: Address


class Company(BaseModel):
    comany_name: str = Field(min_length=3, max_length=50)
    address: Address
    employees: list[Employee]


emp_1: Employee = Employee(
    employee_id="EMP-101",
    name="Tejas Dixit",
    email="tejasdixit17@gmail.com",
    address=Address(city="Pune", pincode="411028", state="Maharashtra"),
)
emp_2: Employee = Employee(
    employee_id="EMP-102",
    name="Swaroop Dixit",
    email="swaroopdixit17@gmail.com",
    address=Address(city="Pune", pincode="411028", state="Maharashtra"),
)

media_vidya: Company = Company(
    comany_name="Media Vidya",
    address=Address(city="Pune", pincode="411028", state="Maharashtra"),
    employees=[emp_1, emp_2],
)


class Department(StrEnum):
    HR = "HR"
    ADMIN = "ADMIN"
    MARKETING = "MARKETING"
    OPERATIONS = "OPERATIONS"


class TestEmployee(BaseModel):
    """
    This class represents Test Employee
    """

    employee_id: str = Field(min_length=7, max_length=7)
    first_name: str = Field(min_length=3, max_length=10)
    middle_name: str | None = None
    last_name: str = Field(min_length=3, max_length=10)
    email: EmailStr
    secondary_email: EmailStr | None = None
    phone_number: str | None = None
    linkedin_url: str | None = None
    department: Department


try:
    test_employee: TestEmployee = TestEmployee(
        employee_id="EMP-108",
        first_name="Tejas",
        middle_name="Vinaykant",
        last_name="Dixit",
        email="tejasdixit17@gmail.com",
        department=Department.ADMIN,
    )

    print(test_employee.model_dump())
    print(test_employee.department)
    print(type(test_employee.department))
    print(test_employee.department == "ADMIN")
    print(test_employee.model_dump_json())

except ValueError as exc:
    print(exc)


try:
    test_employee_2: TestEmployee = TestEmployee(
        employee_id="EMP-102",
        first_name="Vignesh",
        last_name="Gawali",
        email="vbg3008@gmail.com",
        department="SALES",
    )

    print(test_employee_2.model_dump())

except ValueError as exc:
    print(exc)
