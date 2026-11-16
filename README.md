# Fundamentals and Setup — Internship Milestones

YuvaIntern DevOps Virtual Internship (Task-based) | Remote | Nov 2026 - Present

## Overview
This repository hosts the completed internship tasks. It demonstrates environment setup with Git/GitHub, core Java concepts, and professional project conventions. All work is published on GitHub.

## Completed Tasks

### Task 1 — Fundamentals and Setup
- Environment setup: Java JDK, Maven, Docker, and a code editor configured and verified
- Version control: Git repository initialized, identity configured, commits made, remote linked, and changes pushed to GitHub
- Milestone: `Greeting.java` — a standalone Java application demonstrating class design, package structure (`com.internship.hello`), and the `main` entry point
- Report: `Fundamentals_and_Setup_Report.docx`

### Task 2 — Core Concepts and Skills
- Core Java concepts: object-oriented design, SOLID principles, design patterns (Singleton, Factory, Observer), and memory management
- Mastery project: a Modular Library System applying the service-repository pattern for loose coupling and reusability
- Quality benchmarks: unit testing with JUnit 5 and JavaDoc documentation
- Report: `Core_Concepts_and_Skills_Report.docx`

## Project Structure
```
fundamentals-and-setup/
├── .gitignore                          # ignores build artifacts, IDE files
├── Core_Concepts_and_Skills_Report.docx # Task 2 report
├── Fundamentals_and_Setup_Report.docx   # Task 1 report
├── README.md
└── src/
    └── com/internship/hello/
        └── Greeting.java                # Task 1 milestone
```

## Conventions
- Java packages: lowercase (`com.internship.hello`); classes: PascalCase
- Branches: `main` is protected; work on `task-<n>-<name>` branches, then merge into `main`
- Commits: short imperative messages ("Add health endpoint")

## Running the Milestone
```bash
javac -d build src/com/internship/hello/Greeting.java
java -cp build com.internship.hello.Greeting
```

Expected output:
```
Hello, World!
Hello, Internship!
```

## Git Workflow
- Task branches created per task (`task-2-core-concepts`)
- Each task merged into `main` via no-ff merge
- All work pushed to origin

## Repository
https://github.com/prasanm1423/fundamentals-and-setup