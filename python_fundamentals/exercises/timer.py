import time
from collections.abc import Callable
from typing import Any


def timer(
    func: Callable[..., Any],
) -> Callable[..., float]:

    def wrapper(
        *args: Any,
        **kwargs: Any,
    ) -> float:

        start_time = time.perf_counter()

        func(*args, **kwargs)

        stop_time = time.perf_counter()

        execution_time = stop_time - start_time

        return execution_time

    return wrapper
