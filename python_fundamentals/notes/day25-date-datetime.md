# Day 25 — Date & DateTime

## Goal

Understand when to use `date` and `datetime` in Pydantic models and how Pydantic validates and parses them.

---

## Business Problem

Using `str` for dates allows inconsistent formats.

```python
"21/07/2026"
"21-07-2026"
"July 21, 2026"
"2026-07-21"
```

Business applications require a consistent and validated date format.

---

## Solution

Use Python's `date` and `datetime` types.

```python
from datetime import date, datetime

joining_date: date
created_at: datetime
```

Pydantic automatically parses valid ISO formatted strings into Python objects.

---

## Syntax

```python
from datetime import date, datetime

class Employee(BaseModel):
    joining_date: date
    created_at: datetime
```

---

## Business Use Cases

### Use `date`

- Employee joining date
- Date of birth
- Manufacturing date
- Invoice due date

### Use `datetime`

- User login
- Payment timestamp
- Order creation
- Audit logs
- Record creation time

---

## Validation

### Python Validation

```python
date(year=2024, month=13, day=1)
```

Result:

```
ValueError
```

Reason:

Python validates the `date()` constructor before Pydantic receives the value.

---

### Pydantic Validation

```python
Employee(
    joining_date="2024-13-01",
)
```

Result:

```
ValidationError
```

Reason:

Pydantic parses the string into a `date`. Invalid values raise a `ValidationError`.

---

## Validation Ownership

| Layer | Responsibility |
|--------|----------------|
| Python | Validates `date()` and `datetime()` constructors |
| Pydantic | Parses raw input into Python `date` and `datetime` objects |
| Business Validators | Business-specific rules (future lessons) |

---

## Common Mistakes

### Wrong

```python
joining_date: str
```

### Correct

```python
joining_date: date
```

---

### Wrong

```python
created_at: str
```

### Correct

```python
created_at: datetime
```

---

### Wrong

Expecting:

```python
date(year=2024, month=13, day=1)
```

to raise:

```
ValidationError
```

Actual:

```
ValueError
```

---

## Key Takeaways

- `date` stores only the calendar date.
- `datetime` stores both date and time.
- Business requirements determine whether to use `date` or `datetime`.
- Python validates constructed `date` and `datetime` objects.
- Pydantic parses raw input and raises `ValidationError` when parsing fails.

---

## Hansei

### Today I Learned

- Difference between `date` and `datetime`.
- Difference between Python validation and Pydantic validation.
- Pydantic parses ISO formatted strings automatically.

### Mistakes I Made

Initially expected invalid `date()` construction to raise a `ValidationError`.

### Why It Happened

I did not distinguish between Python runtime validation and Pydantic model validation.

### Improvement

Before debugging, identify which layer owns the validation.

---

## Interview Questions

1. When should you use `date` instead of `datetime`?
2. Why should dates not be stored as `str`?
3. What is the difference between `ValueError` and `ValidationError`?
4. How does Pydantic handle ISO formatted date strings?
5. Which layer owns the validation of `date()`?

---

## Summary

- Business requirement decides `date` vs `datetime`.
- Python validates constructors.
- Pydantic parses and validates input.
- Use `date` for calendar dates.
- Use `datetime` when time is required.
