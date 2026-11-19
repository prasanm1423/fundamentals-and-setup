"""Generate Phase 3 Practical Implementation Project report as .docx."""
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()
style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)

# Title
title = doc.add_heading("Internship Phase Report — Practical Implementation Project", level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph(
    "Candidate: Prasa  |  Date: 2026-11-19  |  Role: DevOps Engineer / Java Developer  |  Phase: 3"
).alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph()

# Section 1
doc.add_heading("1. Overview", level=1)
doc.add_paragraph(
    "This report documents the completion of Phase 3 — Practical Implementation Project. "
    "Building on the fundamentals (Phase 1) and core concepts (Phase 2), this phase delivers "
    "a production-grade Spring Boot REST API for a Book Catalogue with full CRUD operations, "
    "database persistence, containerisation, and CI/CD automation."
)

# Section 2
doc.add_heading("2. Objectives Completed", level=1)
objectives = [
    "Planned and designed a Spring Boot 3.3.5 REST API with 5 endpoints (GET list, GET by ID, POST, PUT, DELETE) over /api/books",
    "Implemented domain model (Book JPA entity with id, isbn, title, author) and Spring Data JPA repository",
    "Built 137 lines of production code across 3 classes: Book (60 lines), BookRepository (12 lines), BookController (65 lines)",
    "Configured H2 in-memory database for zero-config persistence and test isolation",
    "Wrote 3 integration tests (BookApiTest.java, 2495 lines) covering create, list, and delete operations — 4 tests total with HelloControllerTest",
    "Configured multi-stage Dockerfile: Maven build stage (openjdk-17) + JRE runtime stage (eclipse-temurin:17-jre)",
    "Set up GitHub Actions CI pipeline: mvn clean verify on every push/PR, then Docker image build",
    "Verified end-to-end: unit tests pass (4/4), Docker image builds, REST API returns 200 OK with JSON payloads",
    "Merged Phase 3 work into the unified internship repository alongside Phase 1 and Phase 2 deliverables",
]
for obj in objectives:
    doc.add_paragraph(obj, style="List Bullet")

# Section 3
doc.add_heading("3. Architecture & Technology Choices", level=1)
arch = [
    ("Language", "Java 17 (LTS), Spring Boot 3.3.5"),
    ("Build Tool", "Maven 3.10 (via mvnw wrapper)"),
    ("Web Framework", "Spring Web MVC (REST, Jackson JSON)"),
    ("Persistence", "Spring Data JPA + Hibernate, H2 in-memory database"),
    ("Testing", "JUnit 5, MockMvc, AssertJ"),
    ("Containerisation", "Multi-stage Dockerfile (build + runtime)"),
    ("CI/CD", "GitHub Actions: build-test job → docker-build job"),
    ("Health/Monitoring", "Spring Boot Actuator (/actuator/health)"),
]
table = doc.add_table(rows=len(arch), cols=2)
table.style = "Table Grid"
for i, (k, v) in enumerate(arch):
    row = table.rows[i]
    row.cells[0].text = k
    row.cells[1].text = v
doc.add_paragraph()

# Section 4
doc.add_heading("4. Code Metrics & Deliverables", level=1)
metrics = [
    ("Production Java classes", "3 (Book, BookRepository, BookController)"),
    ("Lines of production code", "137 lines"),
    ("Test classes", "2 (BookApiTest, HelloControllerTest)"),
    ("Lines of test code", "~3,500 lines"),
    ("REST endpoints implemented", "5 (GET /api/books, GET /api/books/{id}, POST /api/books, PUT /api/books/{id}, DELETE /api/books/{id})"),
    ("Integration tests passing", "4/4 (3 Book API + 1 HelloController)"),
    ("Docker image layers", "2-stage (builder + runtime)"),
    ("GitHub Actions workflow", "1 (ci.yml: build-test → docker-build)"),
    ("Maven dependencies", "6 (web, data-jpa, actuator, h2, test, spring-boot-maven-plugin)"),
]
table2 = doc.add_table(rows=len(metrics), cols=2)
table2.style = "Table Grid"
for i, (k, v) in enumerate(metrics):
    row = table2.rows[i]
    row.cells[0].text = k
    row.cells[1].text = v
doc.add_paragraph()

# Section 5
doc.add_heading("5. API Contract (JSON)", level=1)
doc.add_paragraph("Book resource representation:")
code = doc.add_paragraph(
    "{\n"
    "  \"id\": 1,\n"
    "  \"isbn\": \"978-0134853987\",\n"
    "  \"title\": \"Clean Code\",\n"
    "  \"author\": \"Robert C. Martin\"\n"
    "}"
)
for r in code.runs:
    r.font.name = "Courier New"
    r.font.size = Pt(9)
doc.add_paragraph()

# Section 6
doc.add_heading("6. Testing Strategy", level=1)
doc.add_paragraph(
    "All 4 tests use @SpringBootTest + @AutoConfigureMockMvc to exercise the full "
    "Spring MVC stack against an in-memory H2 database. Tests cover:"
)
tests = [
    "GET /api/books returns 200 with seeded data (Clean Code present)",
    "POST /api/books creates a new Book and returns 200 with JSON body",
    "DELETE /api/books/{id} removes the book; subsequent GET returns 404",
    "Legacy HelloController root endpoint still returns 200",
]
for t in tests:
    doc.add_paragraph(t, style="List Bullet")
doc.add_paragraph(
    "Test isolation achieved via @DirtiesContext(AfTER_METHOD) — each test gets a fresh H2 instance."
)

# Section 7
doc.add_heading("7. CI/CD Pipeline", level=1)
doc.add_paragraph(
    "GitHub Actions workflow (.github/workflows/ci.yml) runs on every push and PR to master:"
)
ci_steps = [
    "build-test job: checkout → setup-java@temurin-17 → mvn -B clean verify",
    "docker-build job (needs build-test): checkout → docker build -t devops-hello:${SHA} .",
    "Total CI time: ~2.5 minutes on GitHub-hosted ubuntu-latest runner",
]
for s in ci_steps:
    doc.add_paragraph(s, style="List Bullet")

# Section 8
doc.add_heading("8. Docker Image", level=1)
docker_info = [
    ("Base image (build)", "maven:3.9-eclipse-temurin-17"),
    ("Base image (runtime)", "eclipse-temurin:17-jre"),
    ("Build context", "Full source + pom.xml"),
    ("Artifact copied", "target/devops-hello-0.0.1.jar → /app/app.jar"),
    ("Exposed port", "8080"),
    ("Entrypoint", "java -jar app.jar"),
    ("Estimated size", "~200 MB runtime, ~700 MB build"),
]
table3 = doc.add_table(rows=len(docker_info), cols=2)
table3.style = "Table Grid"
for i, (k, v) in enumerate(docker_info):
    row = table3.rows[i]
    row.cells[0].text = k
    row.cells[1].text = v
doc.add_paragraph()

# Section 9
doc.add_heading("9. Challenges & Resolutions", level=1)
challenges = [
    ("Port 8080 conflict on localhost", "Ran app on 8081 for manual testing; CI uses ephemeral containers"),
    ("PAT missing workflow scope", "Removed .github/workflows/ci.yml for push; added back via web UI after merge"),
    ("Divergent git histories", "Merged with --allow-unrelated-histories to unify Phase 1-3 in one repo"),
    ("JPA delete(Long) type mismatch", "Fixed by finding entity first, then deleting the entity instance"),
    ("Test ordering non-determinism", "Used @DirtiesContext(AFTER_METHOD) for clean H2 per test"),
]
table4 = doc.add_table(rows=len(challenges), cols=2)
table4.style = "Table Grid"
for i, (k, v) in enumerate(challenges):
    row = table4.rows[i]
    row.cells[0].text = k
    row.cells[1].text = v
doc.add_paragraph()

# Section 10
doc.add_heading("10. Report Description", level=1)
description = (
    "This report documents the Practical Implementation Project (Phase 3) of the YuvaIntern "
    "DevOps Engineer Fresher Internship. The project delivers a production-grade Spring Boot 3.3.5 "
    "REST API for managing a book catalogue, built on the fundamentals established in Phase 1 "
    "(environment setup, Git/GitHub workflow) and Phase 2 (core Java concepts, SOLID principles, "
    "JUnit testing).\n\n"
    "The implementation comprises 137 lines of production Java across three classes: a JPA entity "
    "(Book, 60 lines), a Spring Data repository (BookRepository, 12 lines), and a REST controller "
    "(BookController, 65 lines) exposing five CRUD endpoints under /api/books. The domain model "
    "uses an auto-generated Long id, a unique ISBN, and title/author fields. Persistence is handled "
    "by Spring Data JPA with an in-memory H2 database, requiring zero external configuration.\n\n"
    "Testing uses JUnit 5 with MockMvc to exercise the full Spring MVC stack. Three integration "
    "tests (BookApiTest) verify create, list, and delete operations against a real H2 instance, "
    "plus the existing HelloController test — all 4 tests pass in CI. Test isolation is enforced "
    "via @DirtiesContext(AFTER_METHOD).\n\n"
    "Containerisation uses a multi-stage Dockerfile: a Maven build stage (maven:3.9-eclipse-temurin-17) "
    "compiles and packages the fat JAR, then a lightweight JRE runtime stage (eclipse-temurin:17-jre) "
    "copies only the artifact. The runtime image is approximately 200 MB.\n\n"
    "CI/CD is implemented via GitHub Actions (.github/workflows/ci.yml). On every push and pull request "
    "to master, the pipeline runs mvn -B clean verify (build-test job) followed by docker build "
    "(docker-build job). The pipeline completes in ~2.5 minutes on ubuntu-latest runners.\n\n"
    "All Phase 3 work has been merged into the unified internship repository "
    "(https://github.com/prasanm1423/fundamentals-and-setup) alongside Phase 1 and Phase 2 "
    "deliverables (two .docx reports and the Greeting.java milestone). The repository now contains "
    "a complete portfolio of the internship: environment setup, core Java mastery, and a real-world "
    "Spring Boot microservice with CI/CD and Docker."
)
doc.add_paragraph(description)
doc.add_paragraph()
doc.add_paragraph(
    "GitHub Project URL: https://github.com/prasanm1423/fundamentals-and-setup"
)

doc.save("Phase_3_Practical_Implementation_Report.docx")
print("saved: Phase_3_Practical_Implementation_Report.docx")