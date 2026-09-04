import sqlite3

conn = sqlite3.connect("../learning.db")

try:
    conn.execute(
        """
                SELECT * FROM employees;
            """
    )
except sqlite3.OperationalError as e:
    print(e)
finally:
    conn.close()
