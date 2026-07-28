
# Assignment 01 — Employee Pydantic Model

## Objective

Build a self-validating `Employee` model using **Pydantic**.

This assignment combines:

* Object-Oriented Programming
* Type Hints
* Pydantic
* `Field`
* `EmailStr`
* `field_validator`
* Instance Methods
* Pytest

---

# Learning Goals

After completing this assignment, you should be able to:

* Create a Pydantic model.
* Validate data using `Field`.
* Write custom validation using `field_validator`.
* Normalize user input.
* Add instance methods to a Pydantic model.
* Test validation using `pytest`.

---

# Requirements

Create a file:

```text
employee.py
```

Create the following model:

```python
class Employee(BaseModel):
```

---

# Fields

Implement the following fields:

| Field       | Type     |
| ----------- | -------- |
| employee_id | str      |
| name        | str      |
| email       | EmailStr |
| salary      | float    |

---

# Validation Rules

## employee_id

Rules:

* Must start with `"EMP-"`.

Example:

```text
EMP-1001
```

Use:

* `field_validator`

---

## name

Rules:

* Remove leading and trailing whitespace.
* Convert to Title Case.
* Minimum length: 3 characters.
* Alphabetic characters only.

Examples:

Valid

```text
"   tejas dixit   "
```

↓

```text
Tejas Dixit
```

Invalid

```text
Tejas123
```

---

## email

Use:

```python
EmailStr
```

---

## salary

Rules:

* Greater than zero.

Use:

```python
Field(gt=0)
```

---

# Instance Methods

Implement the following methods.

---

## annual_salary()

Returns:

```text
monthly salary × 12
```

Example:

```python
employee.annual_salary()
```

---

## apply_raise()

Accepts:

```python
percentage: float
```

Updates the employee salary.

Example:

Before

```text
25000
```

After

```python
employee.apply_raise(10)
```

↓

```text
27500
```

This is a **state-changing method**.

---

# Demonstration

Create:

* One valid employee.
* One invalid email example.
* One invalid name example.
* One invalid salary example.

Catch:

```python
ValidationError
```

Print the validation errors.

---

# Testing

Create:

```text
test_employee.py
```

Write at least four tests.

Required:

* Valid employee
* Invalid email
* Annual salary
* Apply raise

---

# Quality Gates

Your solution must pass:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy .
uv run pytest -v
```

---

# Constraints

* Use type hints everywhere.
* Write docstrings for all public methods.
* Do not use `input()`.
* Do not use global variables.
* Keep validation inside the model.

---

# Expected Learning Outcome

By completing this assignment, you should understand that a **Pydantic model is still a Python class**.

It can contain:

* Fields
* Validators
* Instance methods
* Business logic

Validation protects the model's data, while methods implement the model's behavior.
