#!/usr/bin/env python3.12
# file_name: day13_email_validation.py
# branch: day13_pydantic_advance

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ValidationError,
    field_validator,
)


class Employee(BaseModel):
    """Represents an employee within the organization."""

    name: str = Field(
        min_length=3,
        max_length=20,
    )
    email: EmailStr
    salary: float = Field(gt=0)

    @field_validator("name")
    @classmethod
    def normalize_and_validate_name(cls, value: str) -> str:
        """
        Normalize and validate an employee name.

        Rules:
        - Remove leading/trailing whitespace.
        - Convert to Title Case.
        - Name must contain at least 3 characters.
        - Name must contain alphabetic characters only.
        """

        value = value.strip().title()

        if len(value) < 3:
            raise ValueError("Name must contain at least 3 characters.")

        if not value.replace(" ", "").isalpha():
            raise ValueError("Name must contain alphabetic characters only.")

        return value


def print_separator() -> None:
    print("-" * 60)


if __name__ == "__main__":
    # ---------------------------------------------------------
    # Valid Employee
    # ---------------------------------------------------------

    try:
        valid_employee = Employee(
            name="   tejas dixit   ",
            email="tejasdixit17@zohomail.in",
            salary=25_000.99,
        )

        print("Valid Employee")
        print(valid_employee.model_dump())

    except ValidationError as error:
        print(error)

    print_separator()

    # ---------------------------------------------------------
    # Invalid Email
    # ---------------------------------------------------------

    try:
        invalid_employee_1: Employee = Employee(
            name="Vignesh Gawali",
            email="invalid-email",
            salary=30_000,
        )

    except ValidationError as error:
        print("Invalid Email")
        print(error)

    print_separator()

    # ---------------------------------------------------------
    # Invalid Name (Contains Digits)
    # ---------------------------------------------------------

    try:
        invalid_employee_2: Employee = Employee(
            name="Tejas123",
            email="tejas@example.com",
            salary=30_000,
        )

    except ValidationError as error:
        print("Invalid Name")
        print(error)

    print_separator()

    # ---------------------------------------------------------
    # Invalid Salary
    # ---------------------------------------------------------

    try:
        invalid_employee_3: Employee = Employee(
            name="Rahul Sharma",
            email="rahul@example.com",
            salary=-5_000,
        )

    except ValidationError as error:
        print("Invalid Salary")
        print(error)
