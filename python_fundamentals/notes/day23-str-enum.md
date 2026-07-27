# Day 23 — StrEnum

## Goal

Understand why `StrEnum` is used for business fields with a fixed set of values and why it is preferred for JSON APIs.

---

## Business Problem

Using `str` allows inconsistent values.

```python
department = "HR"
department = "hr"
department = "Human Resource"
department = "Human Resources"
```

Although they represent the same department, they produce inconsistent data.

---

## Solution

Use `StrEnum` when a business field has a predefined set of valid values.

```python
from enum import StrEnum

class Department(StrEnum):
    ADMIN = "ADMIN"
    TECH = "TECH"
    DATA = "DATA"
    CONTENT = "CONTENT"
```

Now only the declared values are accepted.

---

## Syntax

```python
from enum import StrEnum

class Department(StrEnum):
    ADMIN = "ADMIN"
    TECH = "TECH"
```

Use inside a model:

```python
department: Department
```

---

## Business Use Cases

- Department
- User Role
- Order Status
- Payment Status
- Task Status
- Account Type

---

## Rules

- Use `StrEnum` only for fixed business values.
- Do not use `str` when only predefined values are allowed.
- Prefer `StrEnum` over `Enum` for API models.
- `StrEnum` improves consistency and prevents invalid values.

---

## Validation

Valid:

```python
department = Department.TECH
```

or

```python
department = "TECH"
```

Invalid:

```python
department = "SALES"
```

Result:

```
ValidationError
```

---

## Output

Python representation:

```python
employee.model_dump()
```

Output:

```python
{
    "department": <Department.TECH: "TECH">
}
```

JSON representation:

```python
employee.model_dump_json()
```

Output:

```json
{
    "department": "TECH"
}
```

---

## Common Mistakes

### Wrong

```python
department: str
```

### Correct

```python
department: Department
```

---

### Wrong

```python
Department.SALES
```

Raises:

```
AttributeError
```

Reason:

`SALES` is not a member of the enum.

---

### Wrong

```python
department="SALES"
```

Raises:

```
ValidationError
```

Reason:

Pydantic validates the input against the allowed enum values.

---

## Key Takeaways

- `StrEnum` represents a fixed set of business values.
- It prevents inconsistent string values.
- It serializes cleanly to JSON.
- It is preferred for FastAPI request and response models.

---

## Hansei

### Today I Learned

- Why business-controlled fields should use `StrEnum`.
- Difference between `Enum` and `StrEnum`.
- Difference between `AttributeError` and `ValidationError`.

### Mistakes I Made

- Expected `Department.SALES` to raise a `ValidationError`.

### Why It Happened

- Python evaluates enum members before Pydantic validation.

### Improvement

- Distinguish between Python runtime errors and Pydantic validation errors.

---

## Interview Questions

1. Why should `Department` be modeled as a `StrEnum` instead of a `str`?
2. What is the difference between `Enum` and `StrEnum`?
3. Why does `Department.SALES` raise an `AttributeError`?
4. When does Pydantic raise a `ValidationError` for an enum?
5. Why is `StrEnum` preferred in FastAPI applications?

---

## Summary

- Fixed business values → `StrEnum`
- Free text → `str`
- Python validates enum members.
- Pydantic validates input values.
- `model_dump_json()` produces API-friendly JSON.
