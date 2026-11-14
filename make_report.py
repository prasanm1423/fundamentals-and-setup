"""Generate the 'Fundamentals and Setup' internship phase report as a .docx (Java version)."""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()
style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)

# Title
title = doc.add_heading("Internship Phase Report — Fundamentals and Setup", level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph(
    "Candidate: Prasa  |  Date: 2026-11-14  |  Role: Java Development  |  Phase: 1"
).alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph()

# Section 1
doc.add_heading("1. Overview", level=1)
doc.add_paragraph(
    "This report documents the completion of the first phase of the internship, "
    "Fundamentals and Setup. This foundational phase is crucial for building a strong "
    "understanding of the essentials and preparing the workspace for success."
)

# Section 2
doc.add_heading("2. Objectives Completed", level=1)
objectives = [
    "Installed all required tools and software: Java SE 26 JDK, code editor, and "
    "verified compilation via javac.",
    "Studied project structure and conventions: package naming (com.internship.hello), "
    "directory organization, and build workflow using standard Java tooling.",
    "Mastered Git and GitHub setup: initialized repository, configured identity, created "
    "commits, linked remote origin, and pushed changes — establishing version control "
    "proficiency essential for professional collaboration.",
    "Completed the first milestone: a Hello World Java application (Greeting.java) that "
    "demonstrates correct compilation and execution end-to-end.",
    "Reviewed team workflows, communication protocols, and best practices for interacting "
    "with mentors and peers.",
    "Read comprehensive documentation and curated learning resources tailored to Java "
    "development and professional engineering workflows.",
    "Completed initial onboarding tasks to get familiar with tools, processes, and team "
    "expectations.",
]
for obj in objectives:
    doc.add_paragraph(obj, style="List Bullet")

# Section 3
doc.add_heading("3. Environment and Tooling", level=1)
env_items = [
    ("Runtime", "Java SE 26 — JRE verified"),
    ("Compiler", "javac from Oracle JDK distribution"),
    ("Editor", "VS Code / IntelliJ IDEA compatible"),
    ("Version Control", "Git with GitHub remote (https://github.com/prasanm1423/fundamentals-and-setup)"),
    ("Project Structure", "Standard Maven-style layout: src/main/java with package directories"),
]
table = doc.add_table(rows=len(env_items), cols=2)
table.style = "Table Grid"
for i, (tool, desc) in enumerate(env_items):
    row = table.rows[i]
    row.cells[0].text = tool
    row.cells[1].text = desc
doc.add_paragraph()

# Section 4
doc.add_heading("4. Project Structure and Conventions", level=1)
doc.add_paragraph(
    "The Java project follows standard conventions used in professional settings:"
)
conventions = [
    "Package naming: com.<company>.<module>, following Oracle's reverse-domain convention.",
    "Source files stored under src/ organized by package hierarchy.",
    "Build output placed in build/ directory, excluded from version control via .gitignore.",
    "Class names use PascalCase; method names use camelCase per Java Style Guide.",
    "Each class includes a short JavaDoc comment explaining its purpose.",
]
for c in conventions:
    doc.add_paragraph(c, style="List Bullet")

# Section 5
doc.add_heading("5. Milestone: Greeting.java", level=1)
doc.add_paragraph(
    "The first milestone is a simple but complete Java application demonstrating core "
    "concepts — class definition, instance methods, and the main entry point. The program "
    "is compiled with javac and executed using java, confirming the entire development "
    "workflow functions correctly."
)
code_block = doc.add_paragraph(
    "package com.internship.hello;\n\n"
    "public class Greeting {\n"
    "    public String greet(String name) {\n"
    "        return \"Hello, \" + name + \"!\";\n"
    "    }\n\n"
    "    public static void main(String[] args) {\n"
    "        Greeting g = new Greeting();\n"
    "        System.out.println(g.greet(\"World\"));\n"
    "        System.out.println(g.greet(\"Internship\"));\n"
    "    }\n"
    "}"
)
for r in code_block.runs:
    r.font.name = "Courier New"
    r.font.size = Pt(9)
doc.add_paragraph()
output_line = doc.add_paragraph("Output:")
output_line.runs[0].bold = True
output_code = doc.add_paragraph(
    "Hello, World!\n"
    "Hello, Internship!"
)
for r in output_code.runs:
    r.font.name = "Courier New"
    r.font.size = Pt(9)

# Section 6
doc.add_heading("6. Next Steps", level=1)
doc.add_paragraph(
    "With the environment configured and the fundamentals established, the next phase "
    "will introduce more advanced Java frameworks (such as Spring Boot), larger-scale "
    "projects, REST API design, and deeper database integration. The Hello World "
    "milestone verified the basic workflow; subsequent work will scale these concepts "
    "to production-grade applications."
)

# Description
doc.add_heading("Report Description", level=1)
description = (
    "This report submits the work completed during the Fundamentals and Setup phase "
    "of my internship, focused on Java development. The phase began with installing all "
    "required tools and software — specifically Java SE 26 JDK, verifying both the "
    "runtime (java) and compiler (javac) are functional, and setting up a code editor "
    "compatible with the project.\n\n"
    "I then studied the project structure and conventions used in professional Java "
    "development. This includes package naming following the reverse-domain convention "
    "(com.internship.hello), organizing source files into package hierarchies under the "
    "src/ directory, and maintaining a clean separation between source code and build "
    "artifacts via .gitignore.\n\n"
    "Setting up version control with Git and GitHub was treated as a critical skill. I "
    "initialized a local repository, configured my Git identity, made my first commit "
    "containing the milestone source code and README documentation, linked the remote "
    "origin to https://github.com/prasanm1423/fundamentals-and-setup, and successfully "
    "pushed the changes — completing the end-to-end Git workflow.\n\n"
    "The first milestone was creating a simple Hello World Java application, "
    "Greeting.java, which demonstrates core Java programming concepts including class "
    "definition, instance methods, parameter passing, string concatenation, and the "
    "main entry point required for standalone Java programs. Compiling with javac and "
    "running with java confirmed that the entire environment works correctly.\n\n"
    "Throughout the phase, I reviewed team workflows, communication protocols, and how to "
    "interact effectively with mentors and peers. Comprehensive documentation on Java "
    "best practices and the Oracle coding standards were reviewed, along with curated "
    "learning resources tailored to professional Java engineering. Initial onboarding "
    "tasks were completed to ensure familiarity with the tools, development processes, "
    "and team expectations.\n\n"
    "By the end of this phase, the development environment is fully configured, the Git "
    "workflow is established, and a solid foundation in Java fundamentals is in place — "
    "ready for the more advanced framework-based and application-level work in the "
    "phases ahead."
)
doc.add_paragraph(description)
doc.add_paragraph()
doc.add_paragraph(
    "GitHub Project URL: https://github.com/prasanm1423/fundamentals-and-setup"
)

out = "Fundamentals_and_Setup_Report.docx"
doc.save(out)
print("saved:", out)

# verify word count of description paragraph
import re
parts = [p.text for p in doc.paragraphs if "Report Description" not in p.text or p.text.strip()]
desc_text = None
in_desc = False
for p in doc.paragraphs:
    if "Report Description" in p.text:
        in_desc = True
        continue
    if in_desc and p.text.strip():
        desc_text = desc_text + " " + p.text if desc_text else p.text
words = len(desc_text.split()) if desc_text else 0
print(f"description words: {words}")
