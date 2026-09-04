from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


def timer(func: F) -> F:
    """Measure and print a function's execution time."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = perf_counter()
        result = func(*args, **kwargs)
        duration = perf_counter() - start
        print(f"{func.__name__} executed in {duration:.6f} seconds")
        return result

    return cast(F, wrapper)
