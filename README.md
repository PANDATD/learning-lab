
# Learning Lab

> A structured, practice-driven repository documenting my journey toward becoming a Python Backend Engineer.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![uv](https://img.shields.io/badge/package%20manager-uv-orange)
![Pytest](https://img.shields.io/badge/tests-pytest-green)
![Mypy](https://img.shields.io/badge/type--checking-mypy-blue)
![Ruff](https://img.shields.io/badge/linter-ruff-red)
![Pydantic](https://img.shields.io/badge/validation-pydantic-purple)

---

## About

This repository contains my daily backend engineering practice.

The goal is **not only to learn Python syntax**, but also to understand how production backend applications are designed and implemented.

Every topic includes:

* Notes
* Practical exercises
* Mini projects
* Tests
* Code reviews
* Best practices

---

# Repository Structure

```text
learning-lab/
│
├── python_fundamentals/
│   ├── exercises/
│   ├── notes/
│   └── tests/
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# Learning Roadmap

## Python Fundamentals

* [x] Functions & Validation
* [x] *args & **kwargs
* [x] Decorators
* [x] Context Managers
* [x] contextlib
* [x] Type Hints
* [x] Dataclasses
* [x] Inventory Mini Project
* [x] Pytest Basics
* [x] TypedDict
* [x] OOP Fundamentals
* [x] Pydantic Basics

---

## Upcoming

* [ ] Advanced Pydantic
* [ ] File Handling
* [ ] SQLite
* [ ] SQL
* [ ] SQLAlchemy ORM
* [ ] Alembic
* [ ] FastAPI
* [ ] Authentication
* [ ] Docker
* [ ] PostgreSQL
* [ ] Testing with Fixtures
* [ ] Dependency Injection
* [ ] Clean Architecture

---

# Notes

| Day    | Topic                  |
| ------ | ---------------------- |
| Day 01 | Functions & Validation |
| Day 02 | *args & **kwargs       |
| Day 03 | Decorators             |
| Day 04 | Context Managers       |
| Day 05 | contextlib             |
| Day 06 | Type Hints             |
| Day 07 | Dataclasses            |
| Day 08 | Inventory Manager      |
| Day 09 | Pytest                 |
| Day 10 | TypedDict              |
| Day 11 | OOP Fundamentals       |
| Day 12 | Pydantic Basics        |

---

# Exercises

Current exercises include:

* Pricing Calculator
* Inventory Manager
* Dataclass Basics
* Context Managers
* Decorator Examples
* Product Manager (OOP)
* Pydantic Basics
* User Validation

---

# Tooling

This repository uses modern Python tooling.

* Python 3.12+
* uv
* Ruff
* Mypy
* Pytest
* Pydantic

---

# Development

Install dependencies

```bash
uv sync
```

Run tests

```bash
uv run pytest
```

Run mypy

```bash
uv run mypy .
```

Run Ruff

```bash
uv run ruff check .
```

Auto-fix Ruff

```bash
uv run ruff check . --fix
```

---

# Learning Philosophy

Every topic follows the same workflow.

```text
Learn
    ↓
Understand
    ↓
Practice
    ↓
Mini Project
    ↓
Notes
    ↓
Code Review
    ↓
Tests
    ↓
Git Commit
```

---

# Current Focus

Currently learning:

* Pydantic
* Runtime Validation
* Backend Engineering Best Practices

Next milestone:

* FastAPI
* SQLAlchemy
* Production-grade Backend APIs

---

# License

This repository is maintained for educational purposes and continuous backend engineering practice.
