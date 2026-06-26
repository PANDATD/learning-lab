import re

from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator

ALLOWED_DEPARTMENTS: frozenset[str] = frozenset(
    {"HR", "MARKETING", "ADMIN", "OPERATIONS"}
)


class Employee(BaseModel):
    employee_id: str = Field(description="Employee ID")
    name: str = Field(
        description="Employee name",
        min_length=3,
        max_length=20,
    )
    email: EmailStr = Field(description="Employee email")
    department: str = Field(description="Employee department")
    salary: float = Field(description="Monthly salary", gt=0)
    age: int = Field(description="Employee age", ge=18, le=60)
    is_active: bool = Field(
        default=False,
        description="Employee active status",
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, name: str) -> str:
        """Validate Employee name and return transomed name"""
        name = " ".join(name.strip().split()).title()

        if not name.replace(" ", "").isalpha():
            raise ValueError("Name must contain only alphabetic characters.")

        return name

    @field_validator("department")
    @classmethod
    def validate_department(cls, department: str) -> str:
        """Validate Department"""
        department = department.strip().upper()

        if department not in ALLOWED_DEPARTMENTS:
            raise ValueError(f"Department must be one of {sorted(ALLOWED_DEPARTMENTS)}")

        return department

    @field_validator("employee_id")
    @classmethod
    def validate_employee_id(cls, employee_id: str) -> str:
        """Validate Employee id"""
        employee_id = employee_id.strip().upper()

        if not re.fullmatch(r"EMP-\d+", employee_id):
            raise ValueError("Employee ID must be in the format EMP-1001.")

        return employee_id

    def annual_salary(self) -> float:
        """Return annual salary."""
        return self.salary * 12

    def apply_raise(self, percentage: float) -> None:
        """Apply a percentage raise and return the updated salary."""

        if percentage <= 0:
            raise ValueError("Percentage must be greater than 0.")

        self.salary += self.salary * (percentage / 100)
        return None


def main() -> None:
    try:
        employee = Employee(
            employee_id="EMP-1001",
            name="Tejas     Dixit",
            email="tejasdixit17@zohomail.in",
            department="hr",
            salary=25000,
            age=25,
            is_active=True,
        )

        print(employee.model_dump())
        print(f"Annual Salary: {employee.annual_salary():,.2f}")
        employee.apply_raise(percentage=10)
        print(f"Updated Salary:{employee.salary}")

    except ValidationError as exc:
        print(exc)


if __name__ == "__main__":
    main()
