
# Day 07 - Dataclasses

## Problem

Dictionaries are flexible but prone to typo-related bugs.

## Example

```python
user = {
    "name": "Madhav",
    "city": "Nagpur",
}
```

## Dataclass

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    city: str
```

## Benefits

Automatically generates:

* `__init__`
* `__repr__`
* `__eq__`

## Mutable Objects

```python
user.city = "Pune"
```

Allowed by default.

## Frozen Dataclass

```python
@dataclass(frozen=True)
class User:
    ...
```

Creates immutable objects.

## Convert To Dictionary

```python
from dataclasses import asdict

data = asdict(user)
```

## Key Learning

Objects use:

```python
user.name
```

Dictionaries use:

```python
data["name"]
```
