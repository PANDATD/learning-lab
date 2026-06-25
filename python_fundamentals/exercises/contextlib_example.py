from collections.abc import Generator
from contextlib import contextmanager
from typing import Any, Literal


@contextmanager
def timer() -> Generator[None, None, None]:
    print("Starting timer...")

    yield

    print("Execution finished.")


with timer():
    print("Running Code")


"""

Problem Statement

Simulate a database session using @contextmanager.

Requirements:

Print "Opening database session...".
Yield a fake session object (a string is fine).
Print "Closing database session...".
Use it with:


"""


@contextmanager
def get_session() -> Generator[Literal["Connected to PostgresSQL"], Any, None]:
    print("Opning database session")
    try:
        yield "Connected to PostgresSQL"
    finally:
        print("Closing database session")


with get_session() as session:
    print(session)
