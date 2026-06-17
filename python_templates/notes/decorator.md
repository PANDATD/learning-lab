# Day 03 - Decorators

## What is a decorator?

A decorator modifies or extends the behavior of a function without changing the original function code.

## Key Concepts

### Decorator Syntax

```python
@timer
def calculate_sum():
    ...
```

Equivalent to:

```python
calculate_sum = timer(calculate_sum)
```

### Why use *args and **kwargs?

The decorator does not know the signature of the function it decorates.

```python
def wrapper(*args, **kwargs):
```

allows forwarding all positional and keyword arguments.

### Why return result?

```python
result = func(*args, **kwargs)
return result
```

This preserves the original function's return value.

### functools.wraps

Without wraps:

```python
greet.__name__
# wrapper
```

With wraps:

```python
greet.__name__
# greet
```

### Timer Decorator Example

Measures execution time using:

```python
time.perf_counter()
```

Useful for profiling slow code.
