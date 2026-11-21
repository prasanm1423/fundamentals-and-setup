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
- Full-stack Spring Boot REST API: Book Catalogue with CRUD endpoints for ISBN, title, author
- Database: Spring Data JPA + H2 in-memory database
- CI/CD: GitHub Actions pipeline (mvn clean verify + Docker build)
- Multi-stage Docker image (~200MB runtime, ~700MB build)
- 3 integration tests covering all 5 REST endpoints
- Report: `Phase_3_Practical_Implementation_Report.docx`
- Source: `src/main/java/com/example/devopshello/`

### Task 4 — Testing Coverage and Quality Assurance
- Unit tests with Mockito (4 tests, ~0.4s execution)
- Integration tests with MockMvc + H2 (5 tests, ~10s execution)
- Performance tests: p95 latency < 500ms SLA
- Total test suite: 11 tests, 100% pass rate
- Test coverage: key controller paths and JPA operations
- CI enforcement: tests run on every push/pull request
- Report: `Phase_4_Testing_Coverage_Report.docx`
- Tests: `src/test/java/com/example/devopshello/`

## Repository Structure
```
devops-hello/
├── Dockerfile                    # Multi-stage build
├── pom.xml                       # Spring Boot 3.3.5 dependencies
├── Core_Concepts_and_Skills_Report.docx
├── Fundamentals_and_Setup_Report.docx
├── Phase_3_Practical_Implementation_Report.docx
├── Phase_4_Testing_Coverage_Report.docx
└── src/
    ├── com/internship/hello/              # Task 1 milestone
    │   └── Greeting.java
    └── main/java/com/example/devopshello/
        ├── DevopsHelloApplication.java
        ├── controller/BookController.java
        ├── model/Book.java
        ├── repository/BookRepository.java
        └── ...
    └── test/java/com/example/devopshello/
        ├── BookApiTest.java
        ├── BookControllerUnitTest.java
        ├── BookPerformanceTest.java
        └── HelloControllerTest.java
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

## Test Results
- **Tests run**: 11/11 passed (100%)
- **Unit tests**: 4 tests (~0.4s)
- **Integration tests**: 5 tests (~10s)
- **Performance test**: 1 test (p95 < 500ms)
- **Total time**: ~17s

## Conventions
- Java packages: lowercase; classes: PascalCase
- Branches: work on `task-<n>-<name>` then merge into `main`
- Commits: short imperative messages ("Add health endpoint")

## Repository
https://github.com/prasanm1423/fundamentals-and-setup
