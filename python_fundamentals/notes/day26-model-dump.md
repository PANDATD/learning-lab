# Day 26 — model_dump()

## Goal

Understand how `model_dump()` serializes a validated Pydantic model and why serialization is important for different business views.

---

## Business Problem

Different consumers require different representations of the same object.

Example:

### HR

- Employee Name
- Joining Date

### Admin

- Employee Name
- Created At

### Public Profile

- Employee Name

The business object remains the same, but the serialized output changes based on business requirements.

---

## Solution

Use `model_dump()` to serialize a validated Pydantic model into a Python dictionary.

```python
employee.model_dump()
```

---

## Syntax

### Serialize Entire Model

```python
employee.model_dump()
```

### Include Fields

```python
employee.model_dump(
    include={"emp_name", "joining_date"}
)
```

### Exclude Fields

```python
employee.model_dump(
    exclude={"created_at"}
)
```

---

## Business Use Cases

- API responses
- HR dashboard
- Admin dashboard
- Public profile
- Logging
- Exporting reports

---

## Serialization Flow

```text
Raw Input
        ↓
Pydantic Validation
        ↓
Employee Model
        ↓
model_dump()
        ↓
Python Dictionary
```

---

## Rules

- `model_dump()` serializes a validated model.
- Validation happens during model creation, not during serialization.
- One model can have multiple serialized representations.
- Prefer `model_dump()` over `__dict__` for Pydantic models.

---

## Common Mistakes

### Wrong

Thinking `model_dump()` validates the model.

### Correct

Validation occurs during model creation.

`model_dump()` only serializes the existing model.

---

### Wrong

```python
employee.__dict__
```

for application serialization.

### Correct

```python
employee.model_dump()
```

---

## Key Takeaways

- Serialization converts a model into a dictionary.
- Business requirements determine which fields are serialized.
- `include` selects specific fields.
- `exclude` hides specific fields.
- Serialization and validation are different stages.

---

## Hansei

### Today I Learned

- Difference between validation and serialization.
- One model can produce multiple business views.
- `model_dump()` returns a Python dictionary.

### Mistakes I Made

Initially thought `model_dump()` performed validation.

### Why It Happened

I associated every Pydantic method with validation.

### Improvement

Separate model creation from model representation.

---

## Interview Questions

1. What is serialization?
2. What does `model_dump()` return?
3. What is the difference between validation and serialization?
4. Why is `model_dump()` preferred over `__dict__`?
5. When should `include` and `exclude` be used?

---

## Summary

- `model_dump()` serializes a validated Pydantic model.
- It returns a standard Python dictionary.
- Use `include` for selected fields.
- Use `exclude` to hide fields.
- The same model can produce multiple business-specific views.
