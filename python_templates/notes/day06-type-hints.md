
# Day 06 - Type Hints and Generics

## Problem Statement

As Python applications grow, it becomes difficult to understand what types of data functions expect and return. Type hints improve readability, tooling support, and early bug detection without changing runtime behavior.

## Key Learnings

### Basic Type Hints

```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

* `name: str` indicates the parameter should be a string.
* `-> str` indicates the function returns a string.

### Type Hints Are Not Runtime Validation

```python
def add(a: int, b: int) -> int:
    return a + b

add("10", "20")
```

Python executes this code and returns:

```python
"1020"
```

Type hints are mainly used by:

* MyPy
* BasedPyright
* IDEs
* Linters

### Generic Types

#### List of Strings

```python
list[str]
```

Example:

```python
["Madhav", "Tejas", "Vignesh"]
```

#### Dictionary

```python
dict[str, int]
```

Example:

```python
{
    "Maths": 100,
    "Python": 99,
}
```

### Nested Types

#### List of Dictionaries

```python
list[dict[str, str]]
```

Example:

```python
[
    {"name": "Madhav", "city": "Pune"},
    {"name": "Tejas", "city": "Nashik"},
]
```

#### Dictionary of Lists

```python
dict[str, list[int]]
```

Example:

```python
{
    "test_series": [89, 99, 100, 99, 0, 60]
}
```

#### Complex Nested Type

```python
list[dict[str, list[int]]]
```

Example:

```python
[
    {"Programming": [100, 99, 100, 78]},
    {"Database": [100, 88, 99, 100]},
]
```

### Return Type None

```python
def process_names(names: list[str]) -> None:
    print(names)
```

`-> None` means the function does not return a meaningful value.

Example:

```python
result = process_names(["Madhav"])
print(result)
```

Output:

```python
None
```

## Why Type Hints Matter

* Improve code readability
* Better IDE autocomplete
* Static analysis with MyPy
* Earlier bug detection
* Self-documenting code
* Commonly used in FastAPI, Pydantic, and SQLAlchemy

## Summary

Today I learned:

* Basic type hints
* Return types
* Generic types
* Nested generic types
* Difference between type hints and runtime validation
* How to read complex type annotations
