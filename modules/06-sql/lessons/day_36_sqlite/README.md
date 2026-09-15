
# Day 36 — Database Design & Normalization

## Overview

Day 36 focused on relational database design and normalization.

The objective was to learn how to convert business requirements into a normalized relational schema while maintaining data integrity and avoiding unnecessary duplication.

---

## Learning Objectives

* Understand database normalization.
* Apply 1NF, 2NF, and 3NF.
* Identify data redundancy and anomalies.
* Separate entities into appropriate tables.
* Design primary-key and foreign-key relationships.
* Model one-to-many relationships.
* Model many-to-many relationships using association tables.
* Apply database constraints.
* Test the resulting schema with SQLite.

---

## Concepts Covered

### Normalization

Normalization organizes relational data so that facts are stored in appropriate places and unnecessary redundancy is minimized.

Levels covered:

```text
1NF → Atomic values

2NF → No partial dependency on a composite key

3NF → No transitive dependency between non-key attributes
```

Mental model:

> The key, the whole key, and nothing but the key.

---

## Relationships

### One-to-Many

```text
Customer 1 ─── N Order
```

Implemented using:

```text
orders.customer_id → customer.customer_id
```

### Many-to-Many

```text
Student N ─── N Course
```

Implemented using:

```text
student
course
enrollment
```

The association table contains the relationship-specific data.

---

## Schema Designed

### Customer

```text
customer
---------
customer_id PK
customer_name
customer_email UNIQUE
```

### Product

```text
product
---------
product_id PK
product_name
product_price
```

### Orders

```text
orders
---------
order_id PK
customer_id FK
order_date
```

### Order Item

```text
order_item
---------
order_item_id PK
order_id FK
product_id FK
quantity
unit_price
```

Relationships:

```text
Customer 1 ─── N Order
Order 1 ─── N OrderItem
Product 1 ─── N OrderItem
```

---

## Constraint Testing

The SQLite implementation was tested against invalid data.

| Constraint    | Test                     | Result   |
| ------------- | ------------------------ | -------- |
| `UNIQUE`      | Duplicate customer email | Rejected |
| `FOREIGN KEY` | Non-existent customer    | Rejected |
| `CHECK`       | Quantity `0`             | Rejected |
| `NOT NULL`    | Required fields          | Enforced |
| `PRIMARY KEY` | Entity identification    | Enforced |

Foreign-key enforcement was enabled with:

```sql
PRAGMA foreign_keys = ON;
```

---

## Many-to-Many Example

Student/course design:

```text
student
---------
student_id
student_name
student_email

course
---------
course_id
course_name

enrollment
---------
enrollment_id
student_id
course_id
enrollment_date
```

Duplicate enrollment prevention:

```sql
UNIQUE(student_id, course_id)
```

This preserves the many-to-many relationship while preventing the same student from being enrolled in the same course more than once.

---

## Practical Takeaways

### Good design

```text
customer
    ↓
orders
    ↓
order_item
    ↑
product
```

Each table has a clear responsibility.

### Poor design

```text
orders
------------------------------------------------
order_id
customer_id
customer_name
customer_email
order_date
```

Customer facts are repeated for every order, creating unnecessary redundancy and potential update anomalies.

---

## Completion Criteria

* [x] Understand 1NF
* [x] Understand 2NF
* [x] Understand 3NF
* [x] Identify redundancy
* [x] Identify update anomalies
* [x] Design normalized entities
* [x] Design one-to-many relationships
* [x] Design many-to-many relationships
* [x] Use association tables
* [x] Apply PK/FK constraints
* [x] Apply `UNIQUE` and `CHECK`
* [x] Implement schema in SQLite
* [x] Test constraint failures
* [x] Complete independent schema-design challenge

## Status

**Day 36 — COMPLETE**

### Next

**Day 37 — Database Indexes**

Focus will move from **schema correctness and data integrity** to **query performance and indexing**.
