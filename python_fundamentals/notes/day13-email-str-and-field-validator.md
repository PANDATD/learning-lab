
# Day 13 — Advanced Pydantic: EmailStr & `field_validator`

## Learning Objectives

By the end of this lesson I learned:

* How to use specialized Pydantic types.
* Why `EmailStr` is better than `str` for email fields.
* How to write custom validation using `@field_validator`.
* How to normalize input before validation.
* How to keep business validation inside the model.
* How to test Pydantic validation using `pytest`.

---

# Why Pydantic?

Python type hints provide static information:

```python
email: str
```

This only tells Python that the field is a string.

Pydantic adds **runtime validation**.

```python
email: EmailStr
```

Now the field must contain a valid email address.

---

# Specialized Types

Instead of using primitive types everywhere, Pydantic provides semantic types.

Example:

```python
from pydantic import EmailStr

email: EmailStr
```

Benefits:

* Validates email addresses.
* Produces meaningful validation errors.
* Makes the model self-documenting.

---

# `Field()`

`Field()` is used to declare validation rules.

Example:

```python
name: str = Field(
    min_length=3,
    max_length=20,
)

salary: float = Field(gt=0)
```

Supported validations include:

* `min_length`
* `max_length`
* `gt`
* `ge`
* `lt`
* `le`
* `default`
* `description`

---

# `field_validator`

`field_validator` allows custom validation that cannot be expressed using `Field()`.

Example:

```python
@field_validator("name")
@classmethod
def normalize_and_validate_name(
    cls,
    value: str,
) -> str:
    ...
```

A validator can:

* Validate values.
* Normalize values.
* Transform values.

---

# Validation Pipeline

When creating a model, validation occurs in this order:

```text
Input
    │
    ▼
Type Conversion
    │
    ▼
Field()
    │
    ▼
field_validator()
    │
    ▼
Model Created
```

Understanding this order helps explain why validators receive values that have already been converted to the declared type.

---

# Normalization Before Validation

A common pattern is:

```python
value = value.strip()
value = value.title()
```

Then validate:

```python
if len(value) < 3:
    raise ValueError(...)
```

Finally:

```python
return value
```

Recommended order:

```text
Normalize
    ↓
Validate
    ↓
Return
```

---

# Returning the Value

Every validator **must** return the final value.

Example:

```python
return value
```

If the value is not returned, the model has nothing to store.

---

# Raising Errors

Inside a validator:

```python
raise ValueError(...)
```

Outside the model:

```python
ValidationError
```

Pydantic automatically converts `ValueError` into `ValidationError`.

---

# Keeping Validation Inside the Model

Instead of:

```python
employee = Employee(...)

if employee.salary < 0:
    ...
```

Prefer:

```python
class Employee(BaseModel):
    ...
```

The model should enforce its own business rules.

---

# Testing Validation

Validation should be tested using `pytest`.

Example:

```python
def test_invalid_email() -> None:
    with pytest.raises(ValidationError):
        Employee(
            name="Tejas Dixit",
            email="invalid-email",
            salary=25_000,
        )
```

Testing validation rules is more reliable than checking printed output.

---

# Best Practices

✔ Use semantic types (`EmailStr`) instead of plain strings.

✔ Keep validation close to the data.

✔ Normalize input before validating.

✔ Return the validated value from every validator.

✔ Raise `ValueError` inside validators.

✔ Test validation using `pytest`.

---

# Concepts Learned

* `BaseModel`
* `EmailStr`
* `Field`
* `field_validator`
* `ValidationError`
* `model_dump()`

---

# Key Takeaways

* Type hints describe the expected type.
* Pydantic validates data at runtime.
* `Field()` handles common validation rules.
* `field_validator()` handles custom business rules.
* Models should protect their own invariants.
* Validation belongs inside the model, not throughout the application.

---

# Summary

Today I learned how to build self-validating models using Pydantic.

I can now:

* Create runtime-validated models.
* Use semantic types like `EmailStr`.
* Normalize incoming data.
* Implement custom validation with `field_validator`.
* Test validation logic using `pytest`.

This completes the foundation required before learning **`model_validator`**, where validation involves relationships between multiple fields.
