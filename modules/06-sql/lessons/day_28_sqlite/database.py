<<<<<<< HEAD
import sqlite3

connection = sqlite3.connect("learning.db")
connection.execute("PRAGMA foreign_keys = ON")  #
# Create depatment table connection.execute( """ CREATE TABLE department( department_id INTEGER PRIMARY KEY, department_name TEXT NOT NULL) """) connection.commit() print("Department Table created.") # Create employee Table. connection.execute( """ CREATE TABLE employee( employee_id INTEGER PRIMARY KEY, employee_name TEXT NOT NULL, employee_email TEXT UNIQUE, department_id INTEGER NOT NULL, salary INTEGER CHECK(salary >=0), FOREIGN KEY (department_id) REFERENCES department(department_id)) """) connection.commit() print("Employee Table Created.")
department_schema = connection.execute("PRAGMA table_info(department)").fetchall()

employee_schema = connection.execute("PRAGMA table_info(employee)").fetchall()
=======
import sqlite3 

connection = sqlite3.connect("learning.db")
connection.execute("PRAGMA foreign_keys = ON")

# Create depatment table


# connection.execute(
#
#     """
#         CREATE TABLE department(
#             department_id INTEGER PRIMARY KEY,
#             department_name TEXT NOT NULL
#
#         )
#     """
# )
# connection.commit()
# print("Department Table created.")

# Create employee Table.

# connection.execute(
#
#     """ CREATE TABLE employee(
#             employee_id INTEGER PRIMARY KEY,
#             employee_name TEXT NOT NULL, 
#             employee_email TEXT UNIQUE, 
#             department_id INTEGER NOT NULL, 
#             salary INTEGER CHECK(salary >=0),
#             FOREIGN KEY (department_id)
#                 REFERENCES department(department_id)
#         )
#     """
# )

# connection.commit()
print("Employee Table Created.")

department_schema = connection.execute(
    "PRAGMA table_info(department)"
).fetchall()

employee_schema = connection.execute(
    "PRAGMA table_info(employee)"
).fetchall()
>>>>>>> 57d847b (created tables)

print("Department Schema: ")
print(department_schema)

print("Employee Schema: ")
print(employee_schema)

<<<<<<< HEAD
foreign_keys = connection.execute("PRAGMA foreign_keys_list(employee)").fetchall()
=======
foreign_keys = connection.execute(
    "PRAGMA foreign_keys_list(employee)"
).fetchall()
>>>>>>> 57d847b (created tables)

print("Employee foreign Keys.")
print(foreign_keys)

print(connection.execute("PRAGMA foreign_keys").fetchone())


<<<<<<< HEAD
# connection.execute(
#     """
#         INSERT INTO department(department_id, department_name)
#         VALUES (1, 'Engineering')
#         """
# )
# connection.commit()

print(
    connection.execute(
        """
            SELECT * FROM department
            """
    ).fetchall()
)


=======
>>>>>>> 57d847b (created tables)
connection.close()
