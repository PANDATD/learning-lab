from typing import ClassVar

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    computed_field,
    field_validator,
)


class Employee(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(
        populate_by_name=True,
    )

    """
    Allow model initialization using both the Python field name (`snake_case`)
    and its alias (for example, `camelCase`).

    This keeps the internal codebase consistent with Python's naming conventions
    while remaining compatible with external APIs that use different field names.
    Without `populate_by_name=True`, Pydantic accepts only the alias for aliased
    fields during validation, which can result in a `ValidationError` when the
    Python field name is provided.
    """

    """This Model represents an employee"""

    first_name: str = Field(
        min_length=3,
        max_length=20,
        alias="firstName",
    )
    last_name: str = Field(min_length=2, max_length=20, alias="lastName")
    monthly_salary: float = Field(gt=0, alias="monthlySalary")

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


try:
    emp1: Employee = Employee(
        firstName="tejas",
        lastName="dixit",
        monthlySalary=25000,
    )

    print(emp1.model_dump())
except ValidationError as exc:
    print(exc)

try:
    emp2: Employee = Employee(
        first_name="swaroop",  # type: ignore
        last_name="dixit",  # type: ignore
        monthly_salary=20000,  # type: ignore
    )
    print(emp2.model_dump())
except ValidationError as exc:
    print(exc)
