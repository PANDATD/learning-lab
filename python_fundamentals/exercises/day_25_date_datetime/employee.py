#!/usr/bin/env python3.12
from datetime import date, datetime

from pydantic import BaseModel, Field, ValidationError


class Employee(BaseModel):
    emp_name: str = Field(min_length=3, max_length=20)
    joining_date: date
    created_at: datetime


try:
    tejas_dixit: Employee = Employee(
        emp_name="Tejas Dixit",
        joining_date=date(year=2024, month=1, day=29),
        created_at=datetime(year=2024, month=1, day=29, hour=13, minute=00, second=20),
    )

    print(f"Python Representaion of Employee Object: {tejas_dixit.model_dump()}")
    print(f"Pydantic Representaion of Employee Object: {tejas_dixit.model_dump_json()}")

    # Use model_validate for string inputs to avoid static type errors and to
    # keep intentional parsing tests.
    vignesh_gawali = Employee.model_validate(
        {"emp_name": "Vignesh Gawali", "joining_date": "2024-12-12", "created_at": "2024-12-12 12:12"}
    )

    print(f"Python Representaion of Employee Object: {vignesh_gawali.model_dump()}")
    print(
        f"Pydantic Representaion of Employee Object: {vignesh_gawali.model_dump_json()}"
    )

except (ValueError, ValidationError) as exc:
    print(exc)
