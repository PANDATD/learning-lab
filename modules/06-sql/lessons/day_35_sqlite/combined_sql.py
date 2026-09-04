import sqlite3


def create_employee(
    employee_id: int,
    employee_name: str,
    employee_email: str,
    department_id: int,
    salary: int,
):

    conn = sqlite3.connect("../learning.db")
    # Connect Database
    try:
        conn.execute("BEGIN TRANSACTION")
        # Begin transaction
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
            (employee_id, employee_name, employee_email, department_id, salary),
        )
        conn.commit()
        # commit if successfull.
    except sqlite3.IntegrityError as e:
        conn.rollback()
        print(e)
        # Handles the integrity error
    except sqlite3.Error as e:
        conn.rollback()
        print(e)
        # Handles the in genral error for fallback
    finally:
        conn.close()
        # cleanup


if __name__ == "__main__":
    # Test 1
    create_employee(
        108,
        "Test Employee",
        "test.employee@gmail.com",
        2,
        50000,
    )
    # Test 2
    create_employee(
        108,
        "Should Not Be Inserted",
        "another.email@gmail.com",
        2,
        60000,
    )
