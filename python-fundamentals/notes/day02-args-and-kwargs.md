
# Day 02 - *args and **kwargs

## Problem

Sometimes the number of arguments is unknown.

## *args

```python
def add(*args):
    print(args)
```

Type:

```python
tuple
```

Example:

```python
add(1, 2, 3)
```

Output:

```python
(1, 2, 3)
```

## **kwargs

```python
def display(**kwargs):
    print(kwargs)
```

Type:

```python
dict
```

Example:

```python
display(name="Madhav")
```

Output:

```python
{"name": "Madhav"}
```

## Key Learning

* `*args` collects positional arguments into a tuple.
* `**kwargs` collects keyword arguments into a dictionary.
