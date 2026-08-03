# create table

## Purpose
Learn how to translate business requirements into a database schema using the `CREATE TABLE` statement.

---

## Definitions

### Schema

A schema is the blueprint of a database that defines tables, columns, constraints, primary keys, and relationships.
---

## Important Commands / Syntax

- To create table use below syntax
```sql
CREATE TABLE table_name (
    column_name DATA_TYPE CONSTRAINTS
);
```
- `.schema` displays the database schema.
- `.schema table_name` displays the schema of a specific table.---

## Key Concepts

- Schema is blueprint of tables


| SQLite Type | Meaning         |
| ----------- | --------------- |
| `NULL`      | Missing value   |
| `INTEGER`   | Whole numbers   |
| `REAL`      | Decimal numbers |
| `TEXT`      | Strings         |
| `BLOB`      | Binary data     |

## Workflow

Business Requirement
        ↓
Entity
        ↓
Attributes
        ↓
Constraints
        ↓
CREATE TABLE

## Mistakes

Initially I thought creating a table meant creating a schema. Now I understand that the schema is the blueprint, and `CREATE TABLE` adds a table definition to that schema.

## Summary

Understand the how to convert buisness requiremet into database design and this databse design into tables.
Buisness requirement -> database schema -> tables.
