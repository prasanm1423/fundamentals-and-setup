# Fundamentals and Setup — Internship Milestones

YuvaIntern DevOps Engineer Fresher Internship (Task-based) | Remote | Nov 2026 - Present

## Overview
This repository hosts the completed internship tasks. It demonstrates environment setup with Git/GitHub, core Java concepts, and a real-world Spring Boot REST API project — all pushed to GitHub with CI via Docker.

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

### Task 3 — Practical Implementation Project
- Full-stack Spring Boot REST API: Book Catalogue with CRUD endpoints
- Database: Spring Data JPA + H2 in-memory database
- CI/CD: GitHub Actions pipeline (mvn clean verify + Docker build)
- Multi-stage Docker image (~200MB runtime, ~700MB build)
- 4 integration tests covering all 5 REST endpoints
- Report: `Phase_3_Pracical_Implementation_Report.docx`

## Repository Structure
```
fundamentals-and-setup/
├── .gitignore
├── .github/workflows/ci.yml    # CI pipeline
├── Core_Concepts_and_Skills_Report.docx   # Task 2
├── Fundamentals_and_Setup_Report.docx     # Task 1
├── make_report.py                # Phase 1 report generator
├── pom.xml                       # Spring Boot dependencies
├── Dockerfile                    # Multi-stage build
└── src/main/java/com/example/devopshello/
    ├── DevopsHelloApplication.java
    ├── HelloController.java      # Legacy hello endpoint
    ├── model/Book.java           # JPA entity
    ├── repository/BookRepository.java
    └── controller/BookController.java  # REST API
```

## API Endpoints
| Method | Path               | Description          |
|--------|--------------------|----------------------|
| GET    | /actuator/health   | Health check         |
| GET    | /api/books         | List all books       |
| GET    | /api/books/{id}    | Get book by ID       |
| POST   | /api/books         | Create a book        |
| PUT    | /api/books/{id}    | Update a book        |
| DELETE | /api/books/{id}    | Delete a book        |

## Build & Run
```bash
# Compile and test
./mvnw clean verify

# Run locally
./mvnw spring-boot:run

# Docker
docker build -t devops-hello .
docker run -p 8080:8080 devops-hello
```

## Conventions
- Java packages: lowercase; classes: PascalCase
- Branches: work on `task-<n>-<name>` then merge into `main`
- Commits: short imperative messages ("Add health endpoint")

## Repository
https://github.com/prasanm1423/fundamentals-and-setup
