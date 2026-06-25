from types import TracebackType
from typing import Literal, Self


class DatabaseSession:
    """A simple context manager that simulates a database session."""

    def __enter__(self) -> Self:
        """Open the simulated database connection."""

        print("Connecting to database...")
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> Literal[True]:
        """Close the simulated database connection."""

        if exc_type is not None:
            print(f"Exception: {exc_value}")

        print("Closing database connection...")
        return True


with DatabaseSession():
    print("Running query...")
    raise RuntimeError("Database connection lost.")
