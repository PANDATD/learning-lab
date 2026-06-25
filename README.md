
# Learning Lab

> **A structured, practice-driven repository documenting my journey toward becoming a Python Backend Engineer.**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![uv](https://img.shields.io/badge/package%20manager-uv-orange)
![Pytest](https://img.shields.io/badge/tests-pytest-green)
![MyPy](https://img.shields.io/badge/type--checking-mypy-blue)
![Ruff](https://img.shields.io/badge/linter-ruff-red)
![Pydantic](https://img.shields.io/badge/validation-pydantic-purple)

---

# About

This repository documents my journey toward becoming a Python Backend Engineer.

The objective is not only to learn Python syntax but also to build production-quality backend applications using modern engineering practices.

Every lesson includes:

* 📖 Notes
* 💻 Practical exercises
* 🧪 Pytest test cases
* 🔍 Code reviews
* 🛠️ Static type checking
* ✅ Best practices

---

# Repository Structure

```text
learning-lab/
│
├── .github/
│   └── workflows/
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
* [x] Advanced Pydantic – EmailStr & `field_validator`

---

## Upcoming

* [ ] Advanced Pydantic – `model_validator`
* [ ] Nested Models
* [ ] File Handling
* [ ] Logging
* [ ] SQLite
* [ ] SQL
* [ ] SQLAlchemy 2.0
* [ ] Alembic
* [ ] FastAPI
* [ ] Authentication
* [ ] Docker
* [ ] PostgreSQL
* [ ] GitHub Actions
* [ ] Testing with Fixtures
* [ ] Dependency Injection
* [ ] Clean Architecture

---

# Notes

| Day | Topic                                            | Status |
| --- | ------------------------------------------------ | :----: |
| 01  | Functions & Validation                           |    ✅   |
| 02  | *args & **kwargs                                 |    ✅   |
| 03  | Decorators                                       |    ✅   |
| 04  | Context Managers                                 |    ✅   |
| 05  | contextlib                                       |    ✅   |
| 06  | Type Hints                                       |    ✅   |
| 07  | Dataclasses                                      |    ✅   |
| 08  | Inventory Manager                                |    ✅   |
| 09  | Pytest Basics                                    |    ✅   |
| 10  | TypedDict                                        |    ✅   |
| 11  | OOP Fundamentals                                 |    ✅   |
| 12  | Pydantic Basics                                  |    ✅   |
| 13  | Advanced Pydantic – EmailStr & `field_validator` |    ✅   |

---

# Exercises

Current exercises include:

* Pricing Calculator
* Inventory Manager
* Context Managers
* Decorators
* Product Manager (OOP)
* Pydantic Basics
* Email Validation
* Custom Field Validators
* User Validation

---

# Tooling

| Tool         | Purpose                          |
| ------------ | -------------------------------- |
| Python 3.12+ | Programming Language             |
| uv           | Package & Environment Management |
| Ruff         | Linter & Formatter               |
| MyPy         | Static Type Checking             |
| Pytest       | Testing Framework                |
| Pydantic     | Runtime Data Validation          |
| pre-commit   | Git Hooks                        |

---

# Quality Gates

Every change must pass the following quality checks before being committed.

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy .
uv run pytest -v
uv run pre-commit run --all-files
```

---

# Development

Install dependencies

```bash
uv sync
```

Run all quality checks

```bash
uv run pre-commit run --all-files
```

Run tests

```bash
uv run pytest -v
```

Run MyPy

```bash
uv run mypy .
```

Run Ruff

```bash
uv run ruff check .
```

Check formatting

```bash
uv run ruff format --check .
```

Automatically fix lint issues

```bash
uv run ruff check . --fix
```

---

# Learning Philosophy

Every lesson follows the same engineering workflow.

```text
Learn
    ↓
Understand
    ↓
Practice
    ↓
Exercise
    ↓
Write Notes
    ↓
Code Review
    ↓
Ruff
    ↓
MyPy
    ↓
Pytest
    ↓
pre-commit
    ↓
Git Commit
    ↓
Push
```

---

# Current Focus

Currently learning:

* Advanced Pydantic
* Runtime Validation
* Custom Field Validation

Next milestone:

* `model_validator`
* Nested Models
* FastAPI Request Validation

---

# Long-Term Goal

Build production-ready backend applications using:

* FastAPI
* SQLAlchemy 2.0
* PostgreSQL
* Docker
* GitHub Actions
* Clean Architecture
* Dependency Injection
* Automated Testing

---

# License

This repository is maintained for educational purposes and continuous backend engineering practice.
