# TaskManager

A progressively built full-stack task manager application evolving from a simple CLI tool into a multi-user web application with authentication and AI-powered features.

---

## Overview

This project is built in phases to mirror how real-world applications evolve—from simple scripts to scalable, full-stack systems.

The goal is to strengthen understanding of:

* Backend architecture
* Data persistence (file-based to database systems)
* Full-stack development with Flask
* User authentication and session management
* AI-driven task prioritization

---

## Tech Stack (Evolving)

* Backend: Python
* Frontend (Phase 2): Flask + HTML/CSS (Jinja templates)
* Storage:

  * Phase 1: JSON file
  * Phase 1.5: SQLite
  * Future: PostgreSQL
* Authentication (Phase 3): Flask sessions + hashed passwords

---

## Features by Phase

### Phase 1: CLI Task Manager (Completed)

**Description:**
A command-line task manager using JSON for persistence.

**Features:**

* Add tasks
* View tasks
* Mark tasks as complete
* Rename tasks
* Delete tasks
* Persistent storage using JSON
* Separation of concerns:

  * `main.py` → CLI interface
  * `taskmanager.py` → business logic
  * `storage.py` → file-based persistence

**Key Concepts Learned:**

* Data modeling (tasks as dictionaries)
* File I/O with JSON
* Separation of concerns
* Basic application architecture

---

### Phase 1.5: SQLite Integration (Completed)

**Description:**
Refactored the application to replace JSON-based storage with a SQLite database, introducing a more scalable and realistic persistence layer.

**What Changed:**

* Replaced full-file reads/writes with database operations
* Introduced a `tasks` table with:

  * `task_id` (auto-increment primary key)
  * `task_title`
  * `task_completed`
* Shifted from:

  * “load → modify → save entire list”
  * to:
  * “insert/update/delete specific rows”

**Architecture Responsibilities:**

* `storage.py` → Handles all database operations (SQL, connections, queries)
* `taskmanager.py` → Handles application logic and validation
* `main.py` → Handles user interaction (CLI)

**Key Concepts Learned:**

* Relational database fundamentals
* SQL operations (INSERT, SELECT, UPDATE, DELETE)
* Auto-incrementing IDs
* Separation of logic vs persistence layers
* Transforming raw DB rows into application-friendly data structures

---

### Phase 2: Web App (Flask Frontend)

**Description:**
Convert the CLI task manager into a web application using Flask.

**Planned Features:**

* Web interface for managing tasks
* HTML templates using Jinja
* Form handling (add/update/delete tasks)
* Improved UI/UX with CSS

**Key Concepts to Learn:**

* Flask routing (`@app.route`)
* Request handling (GET/POST)
* Template rendering
* Connecting frontend to backend logic

---

### Phase 3: User Authentication (Login System)

**Description:**
Introduce multi-user support with authentication.

**Planned Features:**

* User registration (signup)
* Login and logout functionality
* Password hashing
* Session management
* User-specific tasks

**Key Concepts to Learn:**

* Authentication vs authorization
* Sessions and cookies
* Secure password storage
* Multi-user data modeling

---

## Future Enhancements

* Upgrade from SQLite to PostgreSQL
* Add due dates and priorities
* Task filtering (completed, overdue, etc.)
* REST API endpoints
* AI-powered task suggestions and prioritization

---

## Project Structure

```id="r0n9cs"
task_manager/
│── main.py          # CLI interface (user interaction)
│── taskmanager.py   # Business logic and validation
│── storage.py       # SQLite database operations
│── tasks.db         # SQLite database file
```

---

## How to Run

### Prerequisites

* Python 3 installed (3.8+ recommended)

---

### Steps

1. Clone the repository:

```
git clone <your-repo-url>
cd task_manager
```

2. Run the application:

```
python main.py
```

---

### What Happens on First Run

* A SQLite database file (`tasks.db`) will be created automatically
* A `tasks` table will be initialized if it does not already exist

---

### Using the Application

* Follow the CLI prompts to:

  * Add tasks
  * View tasks
  * Edit tasks
  * Mark tasks as complete
  * Delete tasks

---

## Goals

* Build strong backend fundamentals
* Understand how applications scale in complexity
* Develop clean, maintainable architecture
* Prepare for full-stack and AI-driven systems

---

## Status

* Phase 1: Complete
* Phase 1.5 (SQLite): Complete
* Phase 2 (Flask): In Progress

---

## What I Would Improve Next
* Better error handling (more edge cases)
* Add a "Goodbye!" message when leaving app
* CLEAN. UP. THE. COMMENTS!

---

## Author Notes

This project is part of a hands-on journey from backend fundamentals to full-stack development and AI integration.

Each phase builds intentionally on the previous one to reflect real-world engineering practices and long-term growth.

If you got this far, you're a real one.
