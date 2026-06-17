"""

Before we move on, create your own context manager:
`class DatabaseSession:`

Requirements:

Connecting to database...
Running query...
Closing database connection...

using:

__enter__()
__exit__()

Keep it simple. No real database needed.

"""


class DatabaseSession:
    """

    This DatabaseSession Context manager
    implemented using __enter__ and __exit__ methods
    """

    def __enter__(self):
        print("Connecting to database")
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        print("Closing database connnection...")


with DatabaseSession() as session:
    print("Running query")
