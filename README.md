# Learning Lab

> **A structured, practice-driven repository documenting my journey toward becoming a Python Backend Engineer.**

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![uv](https://img.shields.io/badge/package%20manager-uv-orange)](https://docs.astral.sh/uv/)
[![Pytest](https://img.shields.io/badge/tests-pytest-green)](https://docs.pytest.org/)
[![MyPy](https://img.shields.io/badge/type--checking-mypy-blue)](https://mypy.readthedocs.io/)
[![Ruff](https://img.shields.io/badge/linter-ruff-red)](https://docs.astral.sh/ruff/)
[![Pydantic](https://img.shields.io/badge/validation-pydantic-purple)](https://docs.pydantic.dev/)

---

## Table of Contents

- [About](#about)
- [Repository Structure](#repository-structure)
- [Learning Roadmap](#learning-roadmap)
- [Progress](#progress)
- [Current Focus](#current-focus)
- [Recent Work](#recent-work)
- [Exercises](#exercises)
- [Tooling](#tooling)
- [Quality Gates](#quality-gates)
- [Development](#development)
- [Learning Workflow](#learning-workflow)
- [Learning Philosophy](#learning-philosophy)
- [Long-Term Goal](#long-term-goal)
- [License](#license)

---

## About

`learning-lab` is my structured practice repository for becoming a Python Backend Engineer.

The repository is organized as progressive modules and focused lessons. The goal is to build backend engineering fundamentals through implementation, verification, documentation, and review rather than passive study alone.

The current learning path is moving from Python and Pydantic fundamentals into relational database concepts, SQL, SQLite, and eventually PostgreSQL, SQLAlchemy 2.0, Alembic, FastAPI, testing, and backend architecture.

---

## Repository Structure

```text
learning-lab/
│
├── .github/
│   └── workflows/
│
├── modules/
│   ├── 01-python-fundamentals/
│   ├── 02-object-oriented-programming/
│   ├── 04-pydantic/
│   ├── 05-databases/
│   └── 06-sql/
│       ├── lessons/
│       │   ├── 01-sqlite-cli/
│       │   ├── 02-create-table/
│       │   ├── day_28_sqlite/
│       │   ├── day_29_sqlite/
│       │   ├── day_30_sqlite/
│       │   ├── day_31_sqlite/
│       │   ├── day_32_sqlite/
│       │   ├── day_33_sqlite/
│       │   ├── day_34_sqlite/
│       │   └── day_35_sqlite/
│       ├── patterns.md
│       └── progress.md
│
├── projects/
├── Makefile
├── pyproject.toml
├── uv.lock
└── README.md
```

The root README is the index. Detailed concepts, exercises, notes, and lesson-specific material live inside their respective module and lesson directories. The current SQL module follows the repository's actual lesson structure from the SQLite CLI and table creation work through Day 35. fileciteturn7file0

---

## Learning Roadmap

### Phase 1 — Python + Pydantic

- [x] Python Fundamentals
- [x] Functions and validation
- [x] `*args` and `**kwargs`
- [x] Decorators
- [x] Context managers and `contextlib`
- [x] Type hints
- [x] Dataclasses
- [x] Pytest basics
- [x] TypedDict
- [x] Object-oriented programming
- [x] Pydantic fundamentals
- [x] Pydantic validators and field constraints
- [x] `EmailStr`
- [x] `field_validator`
- [x] `model_validator`
- [x] `computed_field`
- [x] `model_validate`
- [x] Model configuration and aliases
- [x] Nested models and model collections
- [x] Enum / StrEnum
- [x] Decimal, date, and datetime handling
- [x] `model_dump()` and serialization
- [x] Employee Management System capstone

**Status: Complete**

### Phase 2 — Database Foundations

#### SQLite / SQL

- [x] SQLite CLI fundamentals
- [x] Table creation and schema constraints
- [x] `PRIMARY KEY`
- [x] `FOREIGN KEY`
- [x] `NOT NULL`
- [x] `UNIQUE`
- [x] `CHECK`
- [x] INSERT and SELECT
- [x] UPDATE and DELETE
- [x] Filtering and sorting
- [x] SQL JOINs
- [x] Aggregation
- [x] `GROUP BY`
- [x] `HAVING`
- [x] Combined SQL queries
- [x] Transactions
- [x] Python `sqlite3` error handling
- [ ] Database design and normalization
- [ ] Database indexes
- [ ] Query analysis and `EXPLAIN`
- [ ] Repository pattern and database access

#### Next Database / Backend Modules

- [ ] PostgreSQL
- [ ] Views
- [ ] SQLAlchemy 2.0
- [ ] Alembic
- [ ] FastAPI
- [ ] REST API design
- [ ] Authentication
- [ ] Dependency Injection
- [ ] Integration testing
- [ ] PostgreSQL + Testcontainers
- [ ] Clean Architecture
- [ ] Microservices

---

## Progress

| Day | Topic | Status |
|---:|---|:---:|
| 01 | Functions & Validation | ✅ |
| 02 | `*args` & `**kwargs` | ✅ |
| 03 | Decorators | ✅ |
| 04 | Context Managers | ✅ |
| 05 | `contextlib` | ✅ |
| 06 | Type Hints | ✅ |
| 07 | Dataclasses | ✅ |
| 08 | Inventory Manager | ✅ |
| 09 | Pytest Basics | ✅ |
| 10 | TypedDict | ✅ |
| 11 | OOP Fundamentals | ✅ |
| 12 | Pydantic Basics | ✅ |
| 13 | Advanced Pydantic Validation | ✅ |
| 24 | `computed_field` & Decimal | ✅ |
| 25 | Date & DateTime | ✅ |
| 26 | `model_dump()` & Serialization | ✅ |
| 27 | Pydantic Capstone / Phase 1 | ✅ |
| 28 | SQLite Constraints & Schema | ✅ |
| 29 | INSERT & SELECT | ✅ |
| 30 | UPDATE & DELETE | ✅ |
| 31 | Filtering & Sorting | ✅ |
| 32 | SQL JOINs | ✅ |
| 33 | Aggregation, `GROUP BY` & `HAVING` | ✅ |
| 34 | Transactions | ✅ |
| 35 | SQLite + Python Error Handling | ✅ |

The current repository state contains completed Day 28–35 SQLite lessons, including dedicated Day 33, Day 34, and Day 35 lesson directories. fileciteturn7file0 fileciteturn8file0

---

## Current Focus

**Current stage: Database Foundations — SQLite / SQL**

The completed SQL sequence is currently:

```text
SQLite Schema & Constraints
          ↓
INSERT / SELECT
          ↓
UPDATE / DELETE
          ↓
Filtering / Sorting
          ↓
JOINs
          ↓
Aggregation
          ↓
GROUP BY / HAVING
          ↓
Transactions
          ↓
Python SQLite Error Handling
```

Day 35 is the latest completed lesson. Its implementation covers `IntegrityError`, `OperationalError`, the broader `sqlite3.Error` hierarchy, rollback handling, and connection cleanup. fileciteturn1file1

---

## Recent Work

Recent commits on `main` show the progression of the SQL module:

| Date | Commit | Work |
|---|---|---|
| 2026-09-04 | `feat(day35): add SQLite error handling and transaction rollback` | SQLite error handling and rollback |
| 2026-09-03 | `feat:SQL Transactions` | SQL transactions |
| 2026-09-03 | `feat: practice aggrigation` | SQL aggregation |
| 2026-09-01 | `feat: practice sqlite joins` | SQL JOINs |
| 2026-09-01 | `feat: practice sqlite filtering and sorting` | Filtering and sorting |
| 2026-08-30 | `feat: practice sqlite insert and select` | INSERT and SELECT |
| 2026-08-29 | `feat: practice sqlite constraints` | SQLite constraints |

This reflects the actual recent `main` history rather than the older Pydantic-focused README. fileciteturn4file0

---

## Exercises

The repository contains practical exercises across the completed modules, including:

- Python functions and validation
- Decorators and context managers
- Inventory and pricing exercises
- OOP exercises
- Pydantic validation and modeling
- Employee Management System capstone
- SQLite schema and constraints
- INSERT / SELECT
- UPDATE / DELETE
- Filtering and sorting
- JOINs
- Aggregation and grouped queries
- Transactions
- Python SQLite exception handling

The Day 35 lesson currently contains `combined_sql.py`, `sqlite_exceptions.py`, `oprational_error.py`, `README.md`, and `notes.md`. fileciteturn8file0

---

## Tooling

| Tool | Purpose |
|---|---|
| Python 3.12+ | Programming language |
| uv | Environment and dependency management |
| Ruff | Linting and formatting |
| Black | Code formatting |
| MyPy | Static type checking |
| Pytest | Testing framework |
| Pydantic | Runtime data validation |
| Alembic | Database migrations |
| Git | Version control |
| pre-commit | Git hooks |

---

## Quality Gates

The repository uses automated quality checks before changes are considered complete.

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy .
uv run pytest -v
uv run pre-commit run --all-files
```

---

## Development

Synchronize the environment:

```bash
uv sync
```

Run tests:

```bash
uv run pytest -v
```

Run Ruff:

```bash
uv run ruff check .
```

Check formatting:

```bash
uv run ruff format --check .
```

Run MyPy:

```bash
uv run mypy .
```

Run pre-commit hooks:

```bash
uv run pre-commit run --all-files
```

Apply supported Ruff fixes:

```bash
uv run ruff check . --fix
```

---

## Learning Workflow

Each lesson follows a repeatable engineering workflow:

```text
Understand
    ↓
Implement
    ↓
Test / Verify
    ↓
Document
    ↓
Review
    ↓
Quality Gates
    ↓
Commit
    ↓
Push
```

The repository is maintained as incremental practice. Each lesson should build on concepts already learned rather than introducing unrelated complexity.

---

## Learning Philosophy

### Practice over passive consumption

Concepts are learned by implementing them, observing their behavior, and documenting the result.

### YAGNI

Only introduce an abstraction when the current problem requires it. Premature repository layers, service layers, interfaces, or framework abstractions are intentionally avoided during foundational exercises.

### Progressive composition

Previously learned concepts are reused in later work:

```text
Python
  ↓
Pydantic
  ↓
SQL
  ↓
SQLite + Python
  ↓
PostgreSQL
  ↓
SQLAlchemy 2.0
  ↓
FastAPI
  ↓
Production Backend Architecture
```

### Documentation is part of the work

Notes, README files, mental models, and query-building patterns are maintained alongside implementation rather than after the fact. The SQL module already contains module-level patterns and progress documentation as part of this structure. fileciteturn6file0

---

## Long-Term Goal

Build production-oriented backend applications using:

- Python
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- Alembic
- Pytest
- Testcontainers
- REST APIs
- Dependency Injection
- Clean Architecture
- Microservices

The goal is to become capable of designing, implementing, testing, debugging, documenting, and maintaining backend systems—not merely producing code that works once.

---

## License

This repository is maintained for educational purposes and continuous backend engineering practice.
