# Day 26 — model_dump()

## Objective

Understand how `model_dump()` serializes a validated Pydantic model into a Python dictionary and how to control serialized output using `include` and `exclude`.

---

## Concepts Covered

- `model_dump()`
- Serialization
- `include`
- `exclude`
- Business Views

---

## Business Use Cases

- HR View
- Admin View
- Public Profile
- API Response
- Logging

---

## Key Learning

- `model_dump()` serializes a validated Pydantic model.
- It returns a standard Python dictionary.
- Use `include` to serialize only required fields.
- Use `exclude` to omit sensitive or unnecessary fields.
- One model can produce multiple business-specific representations.

---

## Run

```bash
uv run python employee.py
```

---

## Expected Output

- Python dictionary representation of the model.
- HR View containing selected fields.
- Admin View excluding selected fields.
- Automatic parsing of ISO formatted strings into Python objects.

---

## Files

```
employee.py
```

---

## Status

✅ Completed
