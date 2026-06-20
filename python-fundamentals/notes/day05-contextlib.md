
# Day 05 - contextlib.contextmanager

## Problem

Writing custom classes for every context manager can be verbose.

## Solution

```python
from contextlib import contextmanager
```

## Example

```python
@contextmanager
def get_session():
    print("Opening")

    try:
        yield "session"
    finally:
        print("Closing")
```

Usage:

```python
with get_session() as session:
    print(session)
```

## Yield Behavior

Before `yield`:

```text
__enter__()
```

After `yield`:

```text
__exit__()
```

## Key Learning

* `yield` splits enter and exit behavior.
* `finally` guarantees cleanup.
* Useful for database sessions and file handling.
