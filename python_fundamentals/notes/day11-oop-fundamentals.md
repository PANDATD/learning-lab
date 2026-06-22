
# Day 11 - OOP Fundamentals

# Problem

As applications grow, related data and behavior should stay together.

Instead of:

```python
calculate_total_price(price, quantity)
```

we can group data and behavior into an object.

This is one of the primary goals of Object-Oriented Programming (OOP).

---

# Core Concepts

## Class

A class is a blueprint used to create objects.

Example:

```python
class Product:
    pass
```

`Product` is a class.

---

## Object / Instance

An object is created from a class.

Example:

```python
mobile = Product()
```

`mobile` is an object (instance) of the `Product` class.

---

# Attributes

Attributes store data inside an object.

Example:

```python
class Product:

    def __init__(
        self,
        name: str,
        price: float,
    ):
        self.name = name
        self.price = price
```

Attributes:

* name
* price

Access:

```python
mobile.name
mobile.price
```

---

# self

`self` represents the current object.

Example:

```python
self.name = name
```

The value passed to the constructor is stored inside the object.

---

# Methods

Methods define behavior for an object.

Example:

```python
class Product:

    def display(self):
        print(
            self.name,
            self.price,
        )
```

Usage:

```python
mobile.display()
```

Methods operate on object data.

---

# Data + Behavior

A core OOP idea:

```text
Object
=
Data
+
Behavior
```

Example:

Data:

```python
name
price
quantity
```

Behavior:

```python
display()
total_price()
apply_discount()
```

---

# Read-Only Methods

A read-only method calculates and returns a value without modifying the object.

Example:

```python
def discounted_price(
    self,
    percentage: float,
):
    return self.price - (
        self.price * percentage / 100
    )
```

Usage:

```python
new_price = mobile.discounted_price(10)
```

The object's state remains unchanged.

---

# State-Changing Methods

A state-changing method modifies object attributes.

Example:

```python
def apply_discount(
    self,
    percentage: float,
):
    self.price = self.price - (
        self.price * percentage / 100
    )
```

Usage:

```python
mobile.apply_discount(10)
```

The object's state changes.

---

# Object State

State is the current value of an object's attributes.

Before:

```python
{
    "name": "Moto G35",
    "price": 12000,
}
```

After:

```python
mobile.apply_discount(10)
```

State becomes:

```python
{
    "name": "Moto G35",
    "price": 10800,
}
```

---

# Class Attributes

Class attributes belong to the class itself and are shared by all objects.

Example:

```python
class Product:
    tax_rate = 0.18
```

Usage:

```python
mobile.tax_rate
laptop.tax_rate
```

Both objects access the same value.

---

# Instance Attributes vs Class Attributes

Instance Attributes:

```python
self.name
self.price
```

Stored separately for each object.

Example:

```text
mobile.price = 12000
laptop.price = 50000
```

---

Class Attributes:

```python
tax_rate = 0.18
```

Shared by all objects.

Example:

```text
mobile.tax_rate = 0.18
laptop.tax_rate = 0.18
```

---

# Why It Matters

Backend applications are full of objects:

```python
User
Product
Order
Invoice
DatabaseSession
```

These objects contain:

* Data
* Business Rules
* State Changes

Examples:

```python
order.mark_paid()
user.activate()
product.apply_discount()
```

---

# Key Learning

* Class = Blueprint
* Object = Instance of a class
* Attributes store data
* Methods define behavior
* self refers to the current object
* Objects combine data and behavior
* Read-only methods calculate values
* State-changing methods modify objects
* Class attributes are shared
* Instance attributes belong to each object
