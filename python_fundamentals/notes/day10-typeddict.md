
# Day 10 - TypedDict

# Problem

Using:

```python
data: dict[str, object]
```

is weak because it does not describe the structure of the dictionary.

Example:

```python
user: dict[str, object] = {
    "name": 123,
    "city": [],
}
```

The type checker knows:

* Keys are strings
* Values are objects

But it does not know:

* What keys are required
* What each value type should be

---

# Concept

`TypedDict` allows us to define a dictionary with a known structure.

Example:

```python
from typing import TypedDict


class User(TypedDict):
    name: str
    email: str
```

Now the type checker understands:

```python
{
    "name": str,
    "email": str,
}
```

---

# Example

```python
from typing import NotRequired, TypedDict


class User(TypedDict):
    name: str
    email: str
    city: NotRequired[str]


user: User = {
    "name": "Tejas Dixit",
    "email": "tejasdixit17@gmail.com",
    "city": "Pune",
}
```

Access values like a normal dictionary:

```python
user["name"]
user["email"]
user["city"]
```

---

# Required and Optional Keys

```python
from typing import NotRequired, TypedDict


class User(TypedDict):
    name: str
    email: str
    city: NotRequired[str]
```

Required keys:

```text
name
email
```

Optional keys:

```text
city
```

Valid:

```python
user: User = {
    "name": "Tejas Dixit",
    "email": "tejasdixit17@gmail.com",
}
```

Also valid:

```python
user: User = {
    "name": "Tejas Dixit",
    "email": "tejasdixit17@gmail.com",
    "city": "Pune",
}
```

---

# Important Notes

TypedDict does NOT perform runtime validation.

Example:

```python
from typing import TypedDict


class User(TypedDict):
    name: str
    email: str


user: User = {
    "name": 123,
    "email": [],
}

print(user)
```

Python executes this successfully.

Type checkers such as:

* mypy
* pyright
* basedpyright

will report errors.

TypedDict is primarily for static type checking.

---

# TypedDict vs Dataclass

## TypedDict

```python
from typing import TypedDict


class User(TypedDict):
    name: str
    email: str
```

Access:

```python
user["name"]
```

Characteristics:

* Dictionary
* JSON-friendly
* API payloads
* Static type checking

---

## Dataclass

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str
```

Access:

```python
user.name
```

Characteristics:

* Object
* Business logic
* Domain models
* Application state

---

# Comparison

```text
dict        -> Generic dictionary
TypedDict   -> Typed dictionary
dataclass   -> Application object
Pydantic    -> Runtime validation
```

---

# When To Use

## Use dict

When structure is unknown or highly dynamic.

Example:

```python
headers: dict[str, str]
```

---

## Use TypedDict

When working with:

* JSON payloads
* API responses
* Request/response structures
* Dictionary-based data

Example:

```python
class UserResponse(TypedDict):
    id: int
    name: str
    email: str
```

---

## Use Dataclass

When working with:

* Business logic
* Domain entities
* Application objects

Example:

```python
@dataclass
class Product:
    name: str
    price: float
```

---

## Use Pydantic

When runtime validation is required.

Example:

```python
class Product(BaseModel):
    name: str
    price: float
```

---

# Key Learning

* TypedDict is a typed dictionary.
* TypedDict remains a normal Python dictionary at runtime.
* Access values using dictionary keys.
* TypedDict improves static type checking.
* Dataclasses are better for application objects and business logic.
* Pydantic adds runtime validation.
* A useful progression in backend development is:

```text
dict
↓
TypedDict
↓
dataclass
↓
Pydantic
```
