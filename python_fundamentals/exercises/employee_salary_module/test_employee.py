import pytest
from pydantic import ValidationError

from .employee import Employee


def test_create_valid_employee() -> None:
    employee = Employee(
        employee_id="EMP-1001",
        name="Tejas Dixit",
        email="tejasdixit17@zohomail.in",
        department="HR",
        salary=25000,
        age=25,
        is_active=True,
    )

    assert employee.employee_id == "EMP-1001"
    assert employee.name == "Tejas Dixit"
    assert employee.department == "HR"
    assert employee.salary == 25000
    assert employee.age == 25
    assert employee.is_active is True


def test_invalid_employee_id() -> None:
    with pytest.raises(ValidationError):
        Employee(
            employee_id="1001",
            name="Tejas Dixit",
            email="tejasdixit17@zohomail.in",
            department="HR",
            salary=25000,
            age=25,
        )


def test_invalid_name() -> None:
    with pytest.raises(ValidationError):
        Employee(
            employee_id="EMP-1001",
            name="Tejas123",
            email="tejasdixit17@zohomail.in",
            department="HR",
            salary=25000,
            age=25,
        )


def test_invalid_email() -> None:
    with pytest.raises(ValidationError):
        Employee(
            employee_id="EMP-1001",
            name="Tejas Dixit",
            email="invalid-email",
            department="HR",
            salary=25000,
            age=25,
        )


def test_invalid_department() -> None:
    with pytest.raises(ValidationError):
        Employee(
            employee_id="EMP-1001",
            name="Tejas Dixit",
            email="tejasdixit17@zohomail.in",
            department="SALES",
            salary=25000,
            age=25,
        )


def test_invalid_salary() -> None:
    with pytest.raises(ValidationError):
        Employee(
            employee_id="EMP-1001",
            name="Tejas Dixit",
            email="tejasdixit17@zohomail.in",
            department="HR",
            salary=-100,
            age=25,
        )


def test_invalid_age() -> None:
    with pytest.raises(ValidationError):
        Employee(
            employee_id="EMP-1001",
            name="Tejas Dixit",
            email="tejasdixit17@zohomail.in",
            department="HR",
            salary=25000,
            age=15,
        )


def test_annual_salary() -> None:
    employee = Employee(
        employee_id="EMP-1001",
        name="Tejas Dixit",
        email="tejasdixit17@zohomail.in",
        department="HR",
        salary=25000,
        age=25,
    )

    assert employee.annual_salary() == 300000


def test_apply_raise() -> None:
    employee = Employee(
        employee_id="EMP-1001",
        name="Tejas Dixit",
        email="tejasdixit17@zohomail.in",
        department="HR",
        salary=25000,
        age=25,
    )

    employee.apply_raise(10)

    assert employee.salary == 27500


def test_apply_raise_invalid_percentage() -> None:
    employee = Employee(
        employee_id="EMP-1001",
        name="Tejas Dixit",
        email="tejasdixit17@zohomail.in",
        department="HR",
        salary=25000,
        age=25,
    )

    with pytest.raises(ValueError):
        employee.apply_raise(0)
