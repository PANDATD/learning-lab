import pytest
from pydantic import ValidationError

from python_fundamentals.exercises.day13_email_validation import Employee


def test_invalid_email() -> None:
    with pytest.raises(ValidationError):
        _: Employee = Employee(
            name="tejas Dixit",
            email="invalid-email",
            salary=25_000,
        )
