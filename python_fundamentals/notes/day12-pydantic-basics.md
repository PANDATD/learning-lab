
# Day 12 - Pydantic Basics

# Lesson Goal

Learn how Pydantic performs **runtime validation**, automatic **type conversion**, and how to define validation rules using `Field()`.

---

# Problem

Type hints and dataclasses describe the expected types, but they do **not** validate data at runtime.

Example:

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int


user = User(
    name=123,
    age=[]
)
```

Python creates the object successfully even though the data is incorrect.

Pydantic solves this problem by validating data while creating the object.

---

# BaseModel

Every Pydantic model inherits from `BaseModel`.

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
```

Creating an object:

```python
user = User(
    name="Tejas",
    age=25,
)
```

Access fields like a normal object:

```python
print(user.name)
print(user.age)
```

---

# Runtime Validation

Pydantic validates data when an object is created.

Valid:

```python
User(
    name="Tejas",
    age=25,
)
```

Invalid:

```python
User(
    name="Tejas",
    age=[],
)
```

Raises:

```text
ValidationError
```

---

# Type Coercion

Pydantic automatically converts compatible values.

Example:

```python
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    quantity: int


product = Product(
    name="Motorola G35",
    price="50000",
    quantity="2",
)
```

Stored values become:

```python
price -> 50000.0
quantity -> 2
```

Types:

```python
type(product.price)      # float
type(product.quantity)   # int
```

---

# ValidationError

If a value cannot be converted into the expected type, Pydantic raises a `ValidationError`.

Example:

```python
Product(
    name="Laptop",
    price="abc",
    quantity=2,
)
```

Result:

```text
ValidationError
```

Reason:

```text
"abc" cannot be converted into float.
```

---

# model_dump()

Convert a Pydantic model into a Python dictionary.

Example:

```python
product.model_dump()
```

Returns:

```python
{
    "name": "Motorola G35",
    "price": 50000.0,
    "quantity": 2,
}
```

Equivalent to:

```python
asdict(dataclass_object)
```

for dataclasses.

---

# model_dump_json()

Convert the model into a JSON string.

Example:

```python
print(product.model_dump_json())
```

Output:

```json
{"name":"Motorola G35","price":50000.0,"quantity":2}
```

Useful when returning API responses.

---

# Field()

`Field()` allows us to define validation rules and metadata.

Think of it as:

```text
Field
=
Type Hint
+
Validation Rules
+
Metadata
```

Example:

```python
from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)
```

---

# Numeric Constraints

Greater Than

```python
price: float = Field(gt=0)
```

Accepts:

```text
1
10
100
```

Rejects:

```text
0
-1
```

---

Greater Than or Equal

```python
price: float = Field(ge=0)
```

Accepts:

```text
0
1
100
```

---

Less Than

```python
discount: int = Field(lt=100)
```

Accepts:

```text
99
```

Rejects:

```text
100
101
```

---

Less Than or Equal

```python
discount: int = Field(le=100)
```

Accepts:

```text
100
```

---

# String Constraints

Minimum Length

```python
username: str = Field(min_length=4)
```

---

Maximum Length

```python
username: str = Field(max_length=20)
```

---

Both Together

```python
username: str = Field(
    min_length=4,
    max_length=20,
)
```

---

# Example

```python
from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(
        min_length=4,
        max_length=20,
    )
    email: str
    age: int = Field(ge=18)
    salary: int = Field(gt=0)
```

---

# Validation Flow

```text
Incoming Data
        │
        ▼
Pydantic Validation
        │
        ▼
Type Conversion
        │
        ▼
Valid Model
```

If validation fails:

```text
Incoming Data
        │
        ▼
ValidationError
```

---

# Comparison

## Dataclass

```python
@dataclass
class User:
    ...
```

* Creates objects
* No runtime validation

---

## TypedDict

```python
class User(TypedDict):
    ...
```

* Static type checking
* No runtime validation

---

## Pydantic

```python
class User(BaseModel):
    ...
```

* Runtime validation
* Automatic type conversion
* Serialization support
* Ideal for APIs

---

# When To Use

Use **Pydantic** when:

* Building FastAPI applications
* Validating API request data
* Validating JSON payloads
* Parsing configuration
* Ensuring runtime type safety

---

# Key Learning

* `BaseModel` is the foundation of every Pydantic model.
* Pydantic validates data during object creation.
* Compatible values are automatically converted.
* Invalid values raise `ValidationError`.
* `Field()` defines validation rules.
* `model_dump()` converts a model into a Python dictionary.
* `model_dump_json()` converts a model into a JSON string.
* Pydantic replaces much of the manual validation code written using `if` statements.

---

# Recap

```text
dict
        ↓
TypedDict
        ↓
dataclass
        ↓
Pydantic BaseModel
        ↓
Field()
        ↓
Runtime Validation
        ↓
FastAPI Request Models
```
