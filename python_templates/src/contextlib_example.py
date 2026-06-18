from contextlib import contextmanager


@contextmanager
def timer():
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
def get_session():
    print("Opning database session")
    try:
        yield "Connected to PostgresSQL"
    finally:
        print("Closing database session")


with get_session() as session:
    print(session)
