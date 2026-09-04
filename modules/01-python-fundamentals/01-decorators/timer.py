from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any, cast, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def timer(func: Callable[P, R]) -> Callable[P, R]:
    """Measure and print a function's execution time."""
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = perf_counter()
        result = func(*args, **kwargs)
        duration = perf_counter() - start
        print(f"{func.__name__} executed in {duration:.6f} seconds")
        return result

    return cast(Callable[P, R], wrapper)
