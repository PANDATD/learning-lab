#!/usr/bin/env python3.12

# model_dump() serializes a validated Pydantic model into a Python dictionary.
# Prefer model_dump() over __dict__ because it supports Pydantic features
# such as include, exclude, aliases and serializers.


from datetime import date, datetime

from pydantic import BaseModel, Field, ValidationError


class Employee(BaseModel):
    """This Model Represents and Employee of an Companay"""

    emp_name: str = Field(min_length=3, max_length=20)
    joining_date: date
    created_at: datetime


def format_emp() -> None:
    print(
        "-" * 120,
        end="\n",
    )


try:
    emp: Employee = Employee(
        emp_name="Tejas Dixit",
        joining_date=date(year=2024, month=1, day=29),
        created_at=datetime(year=2024, month=1, day=25, hour=9, minute=30),
    )

    print(
        f"HR View: {emp.model_dump(include={'emp_name', 'joining_date'})}"
    )  # exclude `created_at` field.

    print(
        f"ADMIN View: {emp.model_dump(exclude={'joining_date'})}"
    )  # excludes `joining_date` and include each field.

    format_emp()

    another_emp: Employee = Employee(
        emp_name="Tejas Dixit",
        joining_date="2024-12-29",
        # Intentional: Pydantic will conert it into date format
        created_at="2024-12-28 12:12",
        # Intentional: Pydantic model will convert it into datetime format
    )

    print(
        f"HR View: {another_emp.model_dump(include={'emp_name', 'joining_date'})}"
    )  # exclude `created_at` field.

    print(f"ADMIN View: {another_emp.model_dump(exclude={'joining_date'})}")


except (ValueError, ValidationError) as exc:
    print(exc)
