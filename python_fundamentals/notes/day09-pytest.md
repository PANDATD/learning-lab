
# Day 09 - Pytest Basics

## Problem

Manually running code and checking output is slow and error-prone.

Example:

```python
result = calculate_discounted_price(
    100,
    2,
    10,
)

print(result)
```

As projects grow, manually verifying behavior becomes difficult.

## Solution

Use pytest to automate verification of code behavior.

---

## First Test

Function:

```python
def calculate_discounted_price(
    price: float,
    quantity: int,
    discount_percentage: float,
) -> float:
    ...
```

Test:

```python
def test_discounted_price():
    result = calculate_discounted_price(
        100,
        2,
        10,
    )

    assert result == 180.0
```

---

## assert

`assert` verifies expectations.

Example:

```python
assert 10 == 10
```

Passes.

Example:

```python
assert 10 == 20
```

Fails.

Mental model:

```text
I expect this expression to be True.
```

---

## Test Discovery

Pytest automatically discovers:

```python
def test_something():
    ...
```

Functions must start with:

```text
test_
```

Example:

```python
test_discounted_price
test_invalid_price
test_inventory_value
```

---

## Test Structure

Repository:

```text
python_fundamentals/
├── exercises/
│   └── pricing.py
│
└── tests/
    └── test_pricing.py
```

---

## Running Tests

Run all tests:

```bash
uv run pytest -v
```

Verbose mode:

```bash
uv run pytest -v
```

---

## Real-World Debugging Lesson

Initial error:

```text
ModuleNotFoundError:
No module named 'python_fundamentals'
```

However:

```python
import python_fundamentals
```

worked inside Python.

### Cause

Pytest and Python can import modules differently.

Python REPL automatically included the current working directory.

Pytest was using a different import mechanism during test collection.

### Fix

Run pytest using:

```bash
uv run pytest --import-mode=importlib -v
```

Permanent configuration:

```toml
[tool.pytest.ini_options]
addopts = "--import-mode=importlib"
```

inside:

```text
pyproject.toml
```

---

## Key Learning

* pytest automates verification of code.
* `assert` is used to validate expectations.
* Test functions should start with `test_`.
* Pytest discovers tests automatically.
* Python imports and pytest imports can behave differently.
* Understanding packages and import paths is important for backend projects.

## Deliverables

Completed:

* First pytest test
* Test discovery
* assert statements
* Package import debugging

Next:

* pytest.raises()
* Testing exceptions
* Inventory Manager tests
* Fixtures
  """
