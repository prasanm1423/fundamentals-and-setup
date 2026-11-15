"""Generate the 'Core Concepts and Skills' internship phase report (Java/Spring focus)."""
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()
style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)

title = doc.add_heading("Internship Phase Report — Core Concepts and Skills", level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph(
    "Candidate: Prasa  |  Date: 2026-11-15  |  Role: Java/Spring Boot Development  |  Phase: 2"
).alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph()

doc.add_heading("1. Overview", level=1)
doc.add_paragraph(
    "This report documents the completion of Phase 2 — Core Concepts and Skills. "
    "This phase was dedicated to deepening expertise in Java and Spring Boot "
    "development, bridging the gap between theoretical foundations and practical "
    "application through hands-on projects, industry standard reviews, and guided tutorials."
)

doc.add_heading("2. Objectives Completed", level=1)
objectives = [
    "Analyzed theoretical foundations of modern Java development, including "
    "multithreading, memory management, and object-oriented design patterns.",
    "Completed hands-on coding exercises applying Java best practices, focusing "
    "on clean code, encapsulation, and modular design.",
    "Developed a mastery project demonstrating core concepts: a modular Java library "
    "system implementing repository and service layers.",
    "Studied professional quality benchmarks, including SOLID principles and "
    "common Java pitfalls to ensure production-grade code.",
    "Participated in knowledge assessment quizzes and technical self-evaluations to "
    "identify and address knowledge gaps.",
    "Engaged in regular mentor feedback sessions, clarifying implementation "
    "strategies and discussing industry-relevant career advice.",
]
for obj in objectives:
    doc.add_paragraph(obj, style="List Bullet")

doc.add_heading("3. Core Technical Skills", level=1)
skills = [
    ("Language", "Java 17+, collections API, generic types"),
    ("Design", "SOLID principles, Design Patterns (Singleton, Factory, Observer)"),
    ("Best Practices", "Unit testing (JUnit 5), documentation (JavaDoc)"),
    ("Version Control", "Advanced Git workflow (feature branching, PRs)"),
]
table = doc.add_table(rows=len(skills), cols=2)
table.style = "Table Grid"
for i, (skill, desc) in enumerate(skills):
    row = table.rows[i]
    row.cells[0].text = skill
    row.cells[1].text = desc
doc.add_paragraph()

doc.add_heading("4. Project Showcase: Modular Library System", level=1)
doc.add_paragraph(
    "The primary project for this phase is a Modular Library System. It implements "
    "a clean separation of concerns using service and repository patterns, ensuring "
    "high maintainability. This project demonstrates mastery of object-oriented "
    "principles and core Java collections."
)

doc.add_heading("5. Report Description", level=1)
description = (
    "This report details the work completed during the 'Core Concepts and Skills' "
    "phase of my Java development internship. The phase was structured around "
    "mastering the theoretical and practical foundations required for building "
    "scalable, production-quality applications. My primary objective was to move "
    "beyond basic syntax and gain deep expertise in core Java principles, "
    "including efficient memory management, thread-safe programming, and the "
    "application of SOLID design patterns. I engaged with industry-expert "
    "tutorials that guided me through complex scenarios, transitioning from simple "
    "demonstrative code to modular, testable software components.\n\n"
    "To solidify these concepts, I architected and built a Modular Library System. "
    "This project serves as a practical application of the service-repository "
    "pattern, emphasizing loose coupling and code reusability. Throughout the "
    "process, I rigorously adhered to industry best practices, such as implementing "
    "comprehensive unit tests with JUnit 5 and maintaining high-quality JavaDoc "
    "documentation. Self-assessment quizzes were utilized periodically to identify "
    "knowledge gaps, which were then successfully bridged through targeted "
    "research and mentor feedback sessions. These one-on-one interactions were "
    "pivotal in clarifying technical misunderstandings and aligning my development "
    "approach with professional benchmarks. By the conclusion of this phase, I "
    "have not only achieved a comprehensive understanding of core Java concepts "
    "but have also acquired the practical confidence to apply these tools to solve "
    "complex engineering challenges in larger, enterprise-level applications."
)
doc.add_paragraph(description)
doc.add_paragraph()
doc.add_paragraph(
    "GitHub Project URL: https://github.com/prasanm1423/fundamentals-and-setup"
)

doc.save("Core_Concepts_and_Skills_Report.docx")
print("saved: Core_Concepts_and_Skills_Report.docx")