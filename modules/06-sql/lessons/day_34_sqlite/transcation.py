import sqlite3

conn = sqlite3.connect("../learning.db")  # Connect Database.
try:
    # INSERT and UPDATE are part of the same transaction.
    conn.execute("""BEGIN TRANSACTION""")
    conn.execute(
        """
        INSERT INTO employee(
                    employee_id,
                    employee_name,
                    employee_email,
                    department_id,
                    salary
        )VALUES(?,?,?,?,?);
        """,
        (109, "Yashraj Waghmare", "yash@gmail.com", 2, 78000),
    )
    conn.execute(
        """
            UPDATE employee SET salary = ?
            WHERE employee_id = ?
        """,
        (-90000, 109),  # Delibaretly assinged the negetive salary to test the rollback
        # transction
    )
    conn.commit()  # Commit Changes to database

except Exception as e:
    conn.rollback()  # Rollback Transaction if any Failuer in database.
    print(f"Exception: {e}")

row = conn.execute("SELECT * FROM employee WHERE employee_id = ?", (109,)).fetchone()

print(row)  # Expected to print inserted user and updated value,If Nonting is wrong.
conn.close()  # Connection close.
