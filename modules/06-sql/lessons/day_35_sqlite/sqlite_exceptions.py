import sqlite3

conn = sqlite3.connect("../learning.db")

try:
    conn.execute("BEGIN TRANSACTION")
    conn.execute(
        """
            INSERT INTO employee(
                employee_id, 
                employee_name, 
                employee_email,
                department_id, 
                salary
            )
            VALUES(?,?,?,?,?) 
            """,
        (107, "Atish Karad", "tejasdixit17@gmail.com", 1, 560000),
    )
    conn.commit()
except sqlite3.IntegrityError as e:
    conn.rollback()
    print(e)
finally:
    conn.close()
