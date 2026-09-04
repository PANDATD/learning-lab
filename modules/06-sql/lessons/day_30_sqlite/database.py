import sqlite3

connection = sqlite3.connect("learning.db")
connection.execute("PRAGMA foreign_keys = ON")

# Update employee 104
connection.execute(
    """
    UPDATE employee
    SET salary = ?
    WHERE employee_id = ?
    """,
    (65000, 104),
)

connection.commit()

# Verify update
row = connection.execute(
    """
    SELECT *
    FROM employee
    WHERE employee_id = ?
    """,
    (104,),
).fetchone()

print("Updated employee:", row)

# Try to update a non-existent employee
cursor = connection.execute(
    """
    UPDATE employee
    SET salary = ?
    WHERE employee_id = ?
    """,
    (70000, 999),
)

print("Updated rows:", cursor.rowcount)

# Delete employee 106
cursor = connection.execute(
    """
    DELETE FROM employee
    WHERE employee_id = ?
    """,
    (106,),
)

print("Deleted rows:", cursor.rowcount)

connection.commit()

# Verify deletion
row = connection.execute(
    """
    SELECT *
    FROM employee
    WHERE employee_id = ?
    """,
    (106,),
).fetchone()

print("Deleted employee:", row)

connection.close()
