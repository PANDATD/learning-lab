# Database Fundamentals

## Mental Model

Business
↓
Entity
↓
Table
↓
Columns
↓
Rows
↓
Primary Key

---

## Definitions

### Database

A database stores data permanently so it remains available after the program exits.

### Entity

A real-world thing about which the business stores information.

Examples:

- Employee
- Product
- Customer
- Order

### Attribute

Information that describes an entity.

Example:

Employee

- employee_id
- employee_name
- email

### Table

Represents one entity in the database.

### Column

Represents one attribute of an entity.

### Row

Represents one instance (record) of an entity.

### Primary Key

A column that uniquely identifies each row.

Properties:

- Unique
- Not NULL
- Stable

---

## Engineering Rules

- Every entity becomes a table.
- Every attribute becomes a column.
- Every row represents one business object.
- Prefer IDs over names for primary keys.

---

## Common Mistakes

❌ Treating attributes as entities.

❌ Using business names as primary keys.

❌ Creating duplicate entities.

---

## Summary

Business
↓

Entity
↓

Table
↓

Columns

↓

Rows

↓

Primary Key




# SQLite Fundamentals

## Mental Model

Python Object
↓
RAM
↓
Lost when program exits

-------------------------

SQLite
↓
Database File (.db)
↓
Persistent Storage

---

## Definitions

### SQLite

A lightweight, serverless relational database that stores all data in a single `.db` file.

### Database File

A file that permanently stores tables, rows, indexes, and database metadata.

### Persistent Storage

Data remains available even after the program exits.

---

## Why SQLite?

- Serverless
- Zero configuration
- Lightweight
- Fast for development and learning
- Uses standard SQL

---

## SQLite vs Python Objects

| Python Object | SQLite |
|--------------|---------|
| Stored in RAM | Stored on Disk |
| Lost on program exit | Persistent |
| Temporary | Permanent |

---

## Engineering Rules

- Use SQLite to learn relational databases.
- One `.db` file can contain multiple tables.
- Never assume what a database contains; inspect it.

---

## Summary

Business Requirement
↓
Need Persistent Storage
↓
SQLite Database
↓
Database File (.db)
