import sqlite3


connection = sqlite3.connect("learning.db")
connection.execute("PRAGMA foreign_keys = ON")


# connection.executemany(
#     """
#     INSERT INTO department (
#         department_id,
#         department_name
#     )
#     VALUES (?, ?)
#     """,
#     [
#         (2, "HR"),
#         (3, "Content"),
#         (4, "Technical"),
#     ],
# )
#
#
# connection.executemany(
#     """
#     INSERT INTO employee (
#         employee_id,
#         employee_name,
#         employee_email,
#         department_id,
#         salary
#     )
#     VALUES (?, ?, ?, ?, ?)
#     """,
#     [
#         (104, "Data Kale", "dattakale@gmail.com", 2, 60000),
#         (105, "Himali Nalawade", "Himalinalawade@mail.com", 3, 45000),
#         (106, "Kavita Kamat", "kamatkavita@gmail.com", 4, 30000),
#     ],
# )
#
#
# connection.commit()

employee = connection.execute(
    """
        SELECT * 
        FROM employee
        WHERE employee_id = ?
        """,
    (999,),
).fetchall()

print(employee)


# departments = connection.execute("SELECT * FROM department").fetchall()
#
# employees = connection.execute("SELECT * FROM employee").fetchall()
#
# print("Departments:", departments)
# print("Employees:", employees)

connection.close()
