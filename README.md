# TaskManager
A progressively built full-stack task manager application designed to evolve from a simple CLI tool into a multi-user web application with authentication and AI integrations.

---

## Overview

This project is being developed in phases to simulate how real-world applications grow over time—from core backend logic to a fully interactive web app with user authentication.

The goal is to strengthen understanding of:

* Backend architecture
* Data persistence
* Full-stack development with Flask
* User authentication and session management
* AI to prioritize tasks

---

## Tech Stack (Planned...subject to change!)

* **Backend:** Python
* **Frontend (Phase 2):** Flask + HTML/CSS (Jinja templates)
* **Storage:**

  * Phase 1: JSON file
  * Future: SQLite / PostgreSQL
* **Authentication (Phase 3):** Flask sessions + hashed passwords

---

## Features by Phase

### Phase 1: CLI Task Manager (Completed)

**Description:**
A command-line based task manager with persistent storage using JSON.

**Features:**

* Add tasks
* View tasks
* Mark tasks as complete
* Rename tasks
* Delete tasks
* Persistent storage using JSON
* Clean separation of concerns:

  * `main.py` → CLI interface
  * `task_manager.py` → business logic
  * `storage.py` → data persistence

**Key Concepts Learned:**

* Data modeling (tasks as dictionaries)
* File I/O with JSON
* Separation of concerns (service vs storage layer)
* Working with lists and dictionaries
* Basic application architecture

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
* Login / logout functionality
* Password hashing (security)
* Session management
* User-specific tasks (each user sees only their own data)

**Key Concepts to Learn:**

* Authentication vs authorization
* Sessions and cookies
* Secure password storage
* Multi-user data modeling

---

## Future Enhancements

* Switch from JSON to a real database (SQLite/PostgreSQL)
* Add due dates and priorities
* Task filtering (completed, overdue, etc.)
* REST API endpoints
* AI-powered task suggestions or summaries

---

## Project Structure (Phase 1)

task_manager/
│── main.py          # CLI interface
│── task_manager.py  # Business logic
│── storage.py       # JSON persistence
│── tasks.json       # Data storage

---

## Goals

This project is focused on:

* Building strong backend fundamentals
* Understanding how applications scale in complexity
* Creating a solid foundation for full-stack + AI development

---

## Status

 Phase 1 Complete
 Phase 2 In Progress

---

## Author Notes
If you got this far, you're a real one.
This project is part of a learning journey from backend fundamentals → full-stack development → AI integration. Each phase builds intentionally on the previous one to reinforce real-world engineering practices.

---
