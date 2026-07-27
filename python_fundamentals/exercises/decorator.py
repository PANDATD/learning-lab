#!/usr/bin/python3.12
# __.utf8__

# Build a custom @timer decorator that:

# Measures function execution time.
# Prints the execution duration.
# Preserves the original function's return value.
# Works with any function signature using *args and **kwargs.
# Preserves function metadata using functools.wraps.

from .timer import timer


@timer
def calculate_sum() -> int:
    total = 0

    for i in range(1_000_000):
        total += i

    return total


@timer
def greet(name: str) -> str:
    return f"Hello {name}"


if __name__ == "__main__":
    print(calculate_sum())
    print(greet(name="Madhav"))
