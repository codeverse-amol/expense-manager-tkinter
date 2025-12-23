# Expense Tracker (Python + Tkinter)

## Overview
This project started as a single-file Tkinter application and was
gradually refactored into an industry-style Clean Architecture.

## Motivation
The goal of this project is to practice:
- Clean Architecture
- Separation of concerns
- SOLID principles
- Dependency Injection
- Real-world refactoring workflow

## Architecture
- Models: Core domain entities
- Services: Business logic
- Repositories: Data access abstraction
- Storage: JSON persistence
- Validators: Input validation rules
- UI: CLI and Tkinter UI
- main.py: Composition root

## Evolution
- v1: Monolithic script
- v2: Extracted models and validation
- v3: Service and repository layers
- v4: Storage abstraction
- v5: Testable architecture

## Tech Stack
- Python
- Tkinter
- JSON
- pytest (planned)
