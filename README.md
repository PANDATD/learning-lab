# Learning Lab

> **A structured, practice-driven repository documenting my journey toward becoming a Python Backend Engineer.**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![uv](https://img.shields.io/badge/package%20manager-uv-orange)
![Pytest](https://img.shields.io/badge/tests-pytest-green)
![MyPy](https://img.shields.io/badge/type--checking-mypy-blue)
![Ruff](https://img.shields.io/badge/linter-ruff-red)
![Pydantic](https://img.shields.io/badge/validation-pydantic-purple)

---

# Table of Contents

* [About](#about)
* [Repository Structure](#repository-structure)
* [Learning Roadmap](#learning-roadmap)
* [Completed Topics](#completed-topics)
* [Exercises](#exercises)
* [Tooling](#tooling)
* [Development Workflow](#development-workflow)
* [Quality Gates](#quality-gates)
* [Development Commands](#development-commands)
* [Learning Philosophy](#learning-philosophy)
* [Current Focus](#current-focus)
* [Future Roadmap](#future-roadmap)
* [License](#license)

---

# About

This repository documents my journey toward becoming a Python Backend Engineer.

The focus is not only on learning Python syntax, but also on building the habits required to develop production-quality backend software.

Every topic includes:

* 📖 Notes
* 💻 Practical exercises
* 🧪 Tests
* 🔍 Code reviews
* 📝 Documentation
* 🛠️ Modern development tooling

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

## Completed Topics

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

## Upcoming Topics

* [ ] Advanced Pydantic
* [ ] Logging
* [ ] pathlib
* [ ] File Handling
* [ ] SQLite
* [ ] SQL
* [ ] SQLAlchemy 2.0
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

| Day | Topic                  | Status |
| --- | ---------------------- | :----: |
| 01  | Functions & Validation |    ✅   |
| 02  | *args & **kwargs       |    ✅   |
| 03  | Decorators             |    ✅   |
| 04  | Context Managers       |    ✅   |
| 05  | contextlib             |    ✅   |
| 06  | Type Hints             |    ✅   |
| 07  | Dataclasses            |    ✅   |
| 08  | Inventory Manager      |    ✅   |
| 09  | Pytest Basics          |    ✅   |
| 10  | TypedDict              |    ✅   |
| 11  | OOP Fundamentals       |    ✅   |
| 12  | Pydantic Basics        |    ✅   |

---

# Exercises

Current exercises include:

* Pricing Calculator
* Inventory Manager
* Context Managers
* Decorators
* Product Manager (OOP)
* Pydantic Basics
* User Validation
* Custom Timer Decorator

---

# Tooling

| Tool       | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Programming Language          |
| uv         | Package & Environment Manager |
| Ruff       | Linter & Formatter            |
| MyPy       | Static Type Checker           |
| Pytest     | Testing Framework             |
| Pydantic   | Runtime Data Validation       |
| Git        | Version Control               |
| pre-commit | Git Hooks                     |

---

# Quality Gates

Every change must pass these checks before it is committed.

```bash
ruff check .
ruff format --check .
mypy .
uv run pytest -v
pre-commit run --all-files
```

---

# Development Commands

Install dependencies

```bash
uv sync
```

Run tests

```bash
uv run pytest -v
```

Run Ruff

```bash
uv run ruff check .
```

Check formatting

```bash
uv run ruff format --check .
```

Run MyPy

```bash
uv run mypy .
```

---

# Development Workflow

```text
Create Branch
      │
      ▼
Write Code
      │
      ▼
Review Code
      │
      ▼
Ruff
      │
      ▼
MyPy
      │
      ▼
Pytest
      │
      ▼
pre-commit
      │
      ▼
Commit
      │
      ▼
Push
      │
      ▼
Pull Request
```

---

# Learning Philosophy

Every topic follows the same process.

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
Quality Gates
    ↓
Git Commit
```

---

# Current Focus

**Currently Learning**

* Advanced Pydantic
* Runtime Validation
* Backend Engineering Best Practices

**Next Milestone**

* SQL
* SQLAlchemy
* FastAPI
* Production-grade Backend APIs

---

# Future Roadmap

* GitHub Actions (CI)
* Docker
* PostgreSQL
* Redis
* Testcontainers
* Production Deployment

---

# License

This repository is maintained for educational purposes and continuous backend engineering practice.
