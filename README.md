# Learning Lab

> **A structured, practice-driven repository for learning Python backend engineering.**

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![uv](https://img.shields.io/badge/package%20manager-uv-orange)](https://docs.astral.sh/uv/)
[![Pytest](https://img.shields.io/badge/tests-pytest-green)](https://docs.pytest.org/)
[![MyPy](https://img.shields.io/badge/type--checking-mypy-blue)](https://mypy.readthedocs.io/)
[![Ruff](https://img.shields.io/badge/linter-ruff-red)](https://docs.astral.sh/ruff/)
[![Pydantic](https://img.shields.io/badge/validation-pydantic-purple)](https://docs.pydantic.dev/)

---

## About

`learning-lab` is a personal practice repository for building Python backend engineering skills through implementation, testing, documentation, and review.

The repository has evolved from small Python exercises into a structured learning path covering Python, object-oriented programming, Pydantic, database fundamentals, SQL, and SQLite. Future work will build toward PostgreSQL, SQLAlchemy, Alembic, FastAPI, API design, integration testing, and backend architecture.

The repository is intentionally a **learning lab**, not a production application. Structure and abstractions are introduced when they help the current learning objective rather than for the sake of complexity.

---

## Repository Structure

```text
learning-lab/
│
├── .github/
│   └── workflows/                  # CI and repository automation
│
├── modules/                        # Structured learning material
│   ├── 01-python-fundamentals/
│   ├── 02-object-oriented-programming/
│   ├── 04-pydantic/
│   ├── 05-databases/
│   └── 06-sql/
│       ├── lessons/                # Focused SQL / SQLite lessons
│       ├── patterns.md             # Reusable SQL patterns
│       └── progress.md             # SQL learning progress
│
├── projects/                      # Work that combines multiple concepts
│   └── 01-employee-management-system/
│
├── Makefile                       # Common development commands
├── pyproject.toml                 # Project and tool configuration
├── uv.lock                        # Locked dependencies
└── README.md                      # Repository index
```

### How to read the structure

**`modules/`** answers: *What concept am I learning?*

Each module contains focused lessons, exercises, and documentation related to a learning area.

**`projects/`** answers: *What can I build by combining what I learned?*

Projects are kept separate from individual lessons so that exercises remain focused while larger applications can combine multiple concepts.

**Root configuration** contains repository-wide tooling rather than lesson-specific code.

---

## Learning Roadmap

### Phase 1 — Python + Pydantic

**Status: Complete**

- [x] Python fundamentals
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
- [x] Field constraints and validators
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

### Phase 2 — Database Foundations

**Current stage: SQLite / SQL**

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

### Upcoming

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

| Days | Area | Status |
|---|---|---|
| 01–10 | Python fundamentals, functions, decorators, context managers, typing, dataclasses, testing | Complete |
| 11 | OOP fundamentals | Complete |
| 12–13 | Pydantic fundamentals and validation | Complete |
| 14–23 | Pydantic progression | Complete |
| 24 | `computed_field` and Decimal | Complete |
| 25 | Date and datetime | Complete |
| 26 | `model_dump()` and serialization | Complete |
| 27 | Employee Management System capstone / Phase 1 | Complete |
| 28 | SQLite constraints and schema | Complete |
| 29 | INSERT and SELECT | Complete |
| 30 | UPDATE and DELETE | Complete |
| 31 | Filtering and sorting | Complete |
| 32 | SQL JOINs | Complete |
| 33 | Aggregation, `GROUP BY`, and `HAVING` | Complete |
| 34 | Transactions | Complete |
| 35 | SQLite + Python error handling | Complete |

The repository currently reaches **Day 35**, with the latest work focused on SQLite error handling and transaction rollback.

---

## Current SQL Progression

```text
SQLite CLI
    ↓
Schema & Constraints
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
Python sqlite3 Error Handling
```

The progression is intentional: first understand how data is stored and queried, then move into query composition, grouped results, transaction boundaries, and database failure handling.

---

## Learning Workflow

Each learning task follows the same engineering cycle:

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
Pull Request
    ↓
Merge
```

This means Git, testing, documentation, and review are part of the learning process—not separate activities added later.

---

## Git & Pull Request Practice

The repository uses small branches, focused commits, and pull requests to practice a realistic development workflow.

### Preferred branch flow

```text
main
  ↑
feature / fix / docs branch
  ↑
focused changes
```

Pull requests should normally use `main` as the base branch and a focused feature or fix branch as the head branch.

### Commit principles

Commits should explain the change clearly and remain reasonably focused.

Preferred style:

```text
feat(sql): add transaction practice
feat(sql): add SQLite error handling
fix(sql): correct rollback handling
test(sql): verify transaction rollback
docs(sql): document transaction behavior
refactor(repo): reorganize learning modules
```

Avoid vague commit messages such as:

```text
1
day12
update
changes
```

The goal is not perfect Git history. The goal is to make the repository history understandable enough to show how the work evolved.

---

## Testing & Quality

Testing is introduced according to the behavior being learned. The repository should not create tests merely to increase test count.

The project uses:

| Tool | Purpose |
|---|---|
| Python 3.12+ | Programming language |
| uv | Environment and dependency management |
| Ruff | Linting and formatting |
| MyPy | Static type checking |
| Pytest | Testing |
| Pydantic | Runtime validation and data modeling |
| Git | Version control |
| pre-commit | Local quality hooks |

As the project reaches database and API work, testing will expand toward database integration tests and PostgreSQL/Testcontainers where they provide real value.

### Quality checks

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy .
uv run pytest -v
uv run pre-commit run --all-files
```

---

## Documentation

Documentation lives close to the work it explains.

Depending on the lesson, this may include:

```text
README.md
notes.md
mental_model.md
problem_statement.md
query-building-pattern.md
patterns.md
```

Not every lesson needs every document. Documentation should exist when it improves understanding, review, or future reference.

---

## Learning Philosophy

### Practice over passive consumption

A concept is not considered learned only because it was read. It should be implemented, observed, verified, and documented.

### Progressive composition

Later work should reuse earlier concepts where appropriate:

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
SQLAlchemy
  ↓
FastAPI
  ↓
Production Backend Engineering
```

### YAGNI

Do not introduce abstractions before the problem requires them.

Repository layers, service layers, interfaces, dependency injection, and clean-architecture boundaries should be introduced when they solve an actual problem in the current project—not simply because they are common backend patterns.

### Repository stability

Large structural changes should be made only when the current structure prevents useful work. Once a structure is good enough, the priority is learning and building rather than continuously reorganizing folders.

---

## Long-Term Goal

Build production-oriented backend systems with:

- Python
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- Alembic
- Pytest
- Testcontainers
- REST APIs
- Authentication
- Dependency Injection
- Clean Architecture
- Microservices

The goal is to become capable of designing, implementing, testing, debugging, documenting, and maintaining backend systems—not simply producing code that works once.

---

## Repository Status

**Current milestone: Day 35 — SQLite + Python Error Handling**

The repository is currently in the database foundations stage. The immediate priority is to complete the remaining database concepts before moving into PostgreSQL and SQLAlchemy.

---

## License

This repository is maintained for educational purposes and continuous backend engineering practice.
