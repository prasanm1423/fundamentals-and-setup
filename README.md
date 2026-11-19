# devops-hello

YuvaIntern DevOps Engineer Fresher Internship — Practical Implementation Project.
A Spring Boot REST API for managing a book catalogue, built, tested, and containerised automatically.

## Tech
- Java 17, Spring Boot 3.3.5, Maven 3.10
- Spring Data JPA + H2 (in-memory database)
- Docker (multi-stage build)
- GitHub Actions (CI)

## Project structure
```
devops-hello/
├── .github/workflows/ci.yml   # CI: mvn clean verify + docker build
├── src/main/java/com/example/devopshello/
│   ├── DevopsHelloApplication.java
│   ├── HelloController.java            # legacy root endpoint
│   ├── model/Book.java                 # JPA entity
│   ├── repository/BookRepository.java  # Spring Data JPA
│   └── controller/BookController.java  # REST API
├── src/test/java/com/example/devopshello/
│   ├── HelloControllerTest.java
│   └── BookApiTest.java                # integration tests (MockMvc + H2)
├── Dockerfile                          # multi-stage build
├── pom.xml
└── README.md
```

## API endpoints
| Method | Path               | Description              |
|--------|--------------------|--------------------------|
| GET    | /api/books         | List all books           |
| GET    | /api/books/{id}    | Get one book by id       |
| POST   | /api/books         | Create a book            |
| PUT    | /api/books/{id}    | Update a book            |
| DELETE | /api/books/{id}    | Delete a book            |

## Conventions
- Java packages: lowercase (`com.example.devopshello`); classes: PascalCase
- Branches: `main` is protected by CI; work on `task-<n>-<name>` branches
- Commits: short imperative messages ("Add health endpoint")

## Run locally
```bash
mvn spring-boot:run
```
Open http://localhost:8080/actuator/health and http://localhost:8080/api/books

## Test the API
```bash
# Create
curl -X POST http://localhost:8080/api/books \
  -H "Content-Type: application/json" \
  -d '{"isbn":"978-0134853987","title":"Clean Code","author":"Robert C. Martin"}'

# List
curl http://localhost:8080/api/books
```

## Run in Docker
```bash
docker build -t devops-hello .
docker run -p 8080:8080 devops-hello
```

## CI
Every push and pull request to `main` runs `mvn clean verify` and builds the Docker image.

## Test results
- 4 tests run, 4 passed (0 failures, 0 errors)
- 3 Book API integration tests + 1 HelloController test
- Build: `mvn clean package` succeeds offline

## Repository
https://github.com/prasanm1423/fundamentals-and-setup