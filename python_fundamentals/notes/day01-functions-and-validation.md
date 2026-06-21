
# Day 01 - Functions and Validation

## Problem

Functions help organize reusable business logic.

## Key Concepts

### Function

```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

### Return vs Print

```python
return value
```

is preferred over:

```python
print(value)
```

because returned values can be reused.

### Validation

Validate inputs before processing.

```python
if price <= 0:
    raise ValueError("Price must be greater than 0")
```

### Exceptions

```python
TypeError
ValueError
```

## Key Learning

* Functions should do one thing.
* Return values instead of printing.
* Validate inputs early.
* Raise meaningful exceptions.
