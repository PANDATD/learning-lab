# Day 28 — SQLite Fundamentals

## Goal

Understand how database constraints are implemented and enforced in SQLite.

## What I Learned

- SQLite database persistence.
- Creating tables with `CREATE TABLE`.
- `PRIMARY KEY`
- `FOREIGN KEY`
- `NOT NULL`
- `UNIQUE`
- `CHECK`
- Referential integrity.
- Enabling foreign-key enforcement with `PRAGMA foreign_keys = ON`.
- Parent and child table dependency.
- Basic transactions with `commit()`.

## Implementation

Created:

- `department` table
- `employee` table

Relationship:

```text
department 1 ───── N employee
