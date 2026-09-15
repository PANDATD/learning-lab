
# Day 36 — Database Design & Normalization

## Objective

Understand relational database design and normalization, then apply the concepts by designing and testing normalized SQLite schemas.

---

## 1. Database Design

Database design is the process of deciding:

* What entities need to be represented.
* What attributes belong to each entity.
* How entities relate to each other.
* Which constraints protect data integrity.

### Core principle

Each table should represent a distinct entity or concept, and its columns should describe that entity.

Example:

```text
customer
---------
customer_id
customer_name
customer_email
```

```text
orders
---------
order_id
customer_id
order_date
```

Customer information belongs to `customer`.

Order information belongs to `orders`.

---

# 2. Data Redundancy

Data redundancy occurs when the same fact is unnecessarily stored multiple times.

Bad design:

```text
orders
------------------------------------------------
order_id | customer_id | customer_name | email
101      | 1           | Amit           | ...
102      | 1           | Amit           | ...
103      | 1           | Amit           | ...
```

Customer information is repeated for every order.

Normalized design:

```text
customer
---------
customer_id
customer_name
customer_email

orders
---------
order_id
customer_id
order_date
```

The customer is stored once and orders reference the customer using `customer_id`.

---

# 3. Database Anomalies

Poorly normalized designs can produce anomalies.

## Update anomaly

If customer information is duplicated across multiple rows, changing the customer's information requires updating multiple rows.

Missing one update can leave inconsistent data.

## Insert anomaly

A poorly designed table may make it difficult to store an entity independently of another entity.

## Delete anomaly

Deleting the last related record can accidentally remove the only stored information about another entity.

---

# 4. First Normal Form — 1NF

A table satisfies 1NF when attributes contain atomic values rather than lists or repeating groups.

Bad:

```text
student_id | courses
1          | Python, SQL, FastAPI
```

Better:

```text
student_id | course_id
1          | 101
1          | 102
1          | 103
```

One cell represents one value.

---

# 5. Second Normal Form — 2NF

2NF requires:

* The table is already in 1NF.
* Non-key attributes depend on the whole primary key.

This is especially important with composite keys.

Example:

```text
order_item
-----------------------------
order_id
product_id
product_name
quantity
```

Assume:

```text
(order_id, product_id)
```

is the composite key.

Dependencies:

```text
product_id → product_name

(order_id, product_id) → quantity
```

`product_name` depends only on `product_id`, not on the complete composite key.

Therefore, `product_name` belongs in `product`.

```text
product
---------
product_id
product_name
product_price
```

while:

```text
order_item
---------
order_id
product_id
quantity
unit_price
```

---

# 6. Third Normal Form — 3NF

3NF requires:

* The table is already in 2NF.
* Non-key attributes depend on the key, not on another non-key attribute.

Example:

```text
employee
---------
employee_id
employee_name
department_id
department_name
```

The dependency is:

```text
employee_id → department_id
department_id → department_name
```

Therefore, `department_name` should be separated into a department entity.

---

# 7. Normalization Shortcut

A useful mental model:

> The key, the whole key, and nothing but the key.

Meaning:

* **The key** → attributes depend on the key.
* **The whole key** → no partial dependency.
* **Nothing but the key** → no transitive dependency.

---

# 8. Entity Relationships

## One-to-Many

Example:

```text
Customer 1 ─── N Order
```

A customer can have multiple orders.

Therefore:

```text
orders.customer_id
    ↓
customer.customer_id
```

The foreign key belongs on the many side.

---

## Category → Product

```text
Category 1 ─── N Product
```

A category can contain many products.

Therefore:

```text
product.category_id
    ↓
category.category_id
```

The foreign key belongs in `product`, not `category`.

---

## Many-to-Many

Example:

```text
Student N ─── N Course
```

A student can take many courses.

A course can have many students.

A direct FK relationship cannot represent this cleanly, so an association table is required:

```text
student
course
enrollment
```

Relationship:

```text
Student 1 ─── N Enrollment N ─── 1 Course
```

---

# 9. Normalized E-commerce Schema

The final design used during the lesson:

```text
customer
---------
customer_id PK
customer_name
customer_email UNIQUE

product
---------
product_id PK
product_name
product_price
category_id FK

orders
---------
order_id PK
customer_id FK
order_date

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

Category 1 ─── N Product
```

Important distinction:

`order_item` represents a product as part of a particular order.

Therefore:

* `product_name` → `product`
* `product_price` → `product`
* `quantity` → `order_item`
* `unit_price` → `order_item`
* `customer_name` → `customer`
* `order_date` → `orders`

---

# 10. SQLite Schema Implementation

The normalized customer/order/product schema was implemented and tested using SQLite.

Important SQLite setting:

```sql
PRAGMA foreign_keys = ON;
```

Schema:

```sql
CREATE TABLE customer (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    customer_email TEXT UNIQUE NOT NULL
);

CREATE TABLE product (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    product_price INTEGER NOT NULL CHECK (product_price > 0)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    FOREIGN KEY (customer_id)
        REFERENCES customer(customer_id)
);

CREATE TABLE order_item (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price INTEGER NOT NULL CHECK (unit_price > 0),
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),
    FOREIGN KEY (product_id)
        REFERENCES product(product_id)
);
```

---

# 11. Constraint Testing

The schema was tested with invalid data.

### Duplicate customer email

Result:

```text
UNIQUE constraint failed
```

### Non-existent customer

Result:

```text
FOREIGN KEY constraint failed
```

### Invalid quantity

Attempting:

```text
quantity = 0
```

Result:

```text
CHECK constraint failed: quantity > 0
```

Therefore the schema successfully enforced:

* `UNIQUE`
* `FOREIGN KEY`
* `CHECK`
* `NOT NULL`
* `PRIMARY KEY`

---

# 12. Student-Course Normalization Exercise

A many-to-many relationship was designed as:

```text
student
---------
student_id PK
student_name
student_email UNIQUE

course
---------
course_id PK
course_name UNIQUE

enrollment
---------
enrollment_id PK
student_id FK
course_id FK
enrollment_date
```

To prevent duplicate enrollment:

```sql
UNIQUE(student_id, course_id)
```

This allows:

```text
Student 1 → Course 101
Student 2 → Course 101
Student 1 → Course 102
```

but prevents:

```text
Student 1 → Course 101
Student 1 → Course 101
```

The uniqueness belongs to the **combination** of `student_id` and `course_id`, not to either column individually.

---

# 13. Key Lessons

1. Design tables around entities/concepts.
2. Store each fact in the table where it belongs.
3. Avoid unnecessary duplication.
4. Use PKs to identify entities.
5. Use FKs to represent relationships.
6. In a one-to-many relationship, the FK normally belongs on the many side.
7. Use association tables for many-to-many relationships.
8. Normalize to protect data integrity and reduce anomalies.
9. Do not confuse normalization with query performance.
10. A normalized schema may require joins when related information is retrieved.

---

# 14. Day 36 Outcome

Completed:

* 1NF
* 2NF
* 3NF
* Data redundancy
* Update anomalies
* Entity separation
* One-to-many relationships
* Many-to-many relationships
* Association tables
* PK/FK design
* Constraint design
* Normalized schema implementation
* SQLite constraint testing
* Independent schema-design challenge
* Normalized vs. denormalized evaluation

**Status: COMPLETE**
