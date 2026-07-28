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
