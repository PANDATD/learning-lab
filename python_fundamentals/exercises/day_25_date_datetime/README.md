# Day 25 — Date & DateTime

## Objective

Understand when to use `date` and `datetime` in Pydantic models and how Pydantic parses ISO formatted strings into Python objects.

---

## Concepts Covered

- `date`
- `datetime`
- Pydantic parsing
- `ValidationError`
- `model_dump()`
- `model_dump_json()`

---

## Business Use Cases

### `date`

- Employee joining date
- Date of birth
- Manufacturing date

### `datetime`

- User login
- Payment timestamp
- Audit logs
- Record creation time

---

## Key Learning

- Use `date` when only the calendar date is required.
- Use `datetime` when both date and time are required.
- Python validates `date()` and `datetime()` constructors.
- Pydantic parses strings into `date` and `datetime` objects.
- Invalid parsed values raise `ValidationError`.

---

## Run

```bash
uv run python employee.py
```

---

## Expected Output

- Successful creation of a valid `Employee`.
- `model_dump()` returns Python objects.
- `model_dump_json()` returns JSON.
- Invalid input raises `ValidationError`.

---

## Files

```
employee.py
```

---

## Status

✅ Completed
