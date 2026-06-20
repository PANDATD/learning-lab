
# Day 08 - Inventory Manager Mini Project

## Objective

Combine previously learned Python concepts into a small backend-style application.

## Concepts Used

* Dataclasses
* Type Hints
* Validation
* Context Managers
* Exception Handling
* asdict()

## Features

### Product Model

```python
@dataclass
class Product:
    name: str
    price: float
    quantity: int
```

### Product Validation

```python
validate_product(product)
```

### Inventory Calculation

```python
calculate_inventory_value(products)
```

### Context Manager

```python
with inventory_session():
```

### Export Products

```python
export_products(products)
```

Uses:

```python
asdict()
```

## Key Learning

This project demonstrated how multiple Python concepts work together in a real application rather than isolated examples.
