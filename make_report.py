"""Generate the 'Fundamentals and Setup' internship phase report as a .docx."""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Base style
style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)

# Title
title = doc.add_heading("Internship Phase Report — Fundamentals and Setup", level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph(
    "Candidate: Prasa  |  Date: 2026-11-14  |  Phase: 1 — Fundamentals and Setup"
).alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph()

# Section 1: Overview
doc.add_heading("1. Overview", level=1)
doc.add_paragraph(
    "This report documents the completion of the first phase of the internship, "
    "Fundamentals and Setup. This foundational phase is critical for building a "
    "strong understanding of the essentials and preparing the workspace for success. "
    "It covers tool installation, environment configuration, project structure and "
    "conventions, role-specific fundamentals, version control setup, the first "
    "milestone, team workflows, documentation review, and initial onboarding tasks."
)

# Section 2: Objectives completed
doc.add_heading("2. Objectives Completed", level=1)
objectives = [
    "Installed all required tools and software specific to the role, including the "
    "development environment, code editor, and frameworks used throughout the program.",
    "Studied the project structure and conventions, learning how files are organized, "
    "naming conventions are applied, and architectural patterns are used in "
    "professional settings.",
    "Dove deep into the fundamentals specific to the chosen role, covering "
    "programming concepts, design principles, and relevant methodologies.",
    "Set up version control with Git and GitHub, a critical skill for tracking "
    "changes, collaborating with team members, and maintaining a professional "
    "portfolio.",
    "Completed the first milestone by creating a simple Hello World project to "
    "verify that the entire environment is working correctly.",
    "Reviewed team workflows, communication protocols, and how to interact with "
    "mentors and peers effectively.",
    "Read comprehensive documentation and curated learning resources tailored to "
    "the specialization.",
    "Completed initial onboarding tasks to get familiar with tools, processes, and "
    "team expectations.",
]
for obj in objectives:
    doc.add_paragraph(obj, style="List Bullet")

# Section 3: Environment and tooling
doc.add_heading("3. Environment and Tooling", level=1)
doc.add_paragraph(
    "The development environment was fully configured with the required interpreter, "
    "an editor, and the frameworks needed for the role. All dependencies were "
    "installed and verified through the Hello World milestone, which confirmed that "
    "code can be written, executed, and debugged end to end. Version control was "
    "initialized with Git and connected to GitHub so that every change is tracked "
    "and collaboration is possible from day one."
)

# Section 4: Project structure and conventions
doc.add_heading("4. Project Structure and Conventions", level=1)
doc.add_paragraph(
    "Understanding how files are organized, how naming conventions are applied, and "
    "which architectural patterns the team uses is essential for contributing "
    "without friction. This phase established a mental model of the repository "
    "layout, the build/run workflow, and the code style expectations, so that new "
    "work fits seamlessly into the existing codebase."
)

# Section 5: Next steps
doc.add_heading("5. Next Steps", level=1)
doc.add_paragraph(
    "With the environment configured and the fundamentals in place, the next phase "
    "will build on this foundation with more advanced work. The Hello World "
    "milestone verified the setup; the focus now shifts to deeper specialization, "
    "larger project tasks, and continued collaboration with mentors and peers."
)

# Description (the evaluator-facing summary, minimum 200 words)
doc.add_heading("Report Description", level=1)
description = (
    "This report submits the work completed during the Fundamentals and Setup "
    "phase of the internship. The phase began with the installation of all required "
    "tools and software specific to the role, including the development environment, "
    "code editor, and the frameworks that will be used throughout the program. A key "
    "part of this phase was understanding the project structure and conventions — "
    "how files are organized, how naming conventions are applied, and which "
    "architectural patterns are used in professional settings. This understanding is "
    "essential for writing code that integrates cleanly with the existing codebase "
    "and aligns with team expectations.\n\n"
    "The fundamentals specific to the chosen role were studied in depth, covering "
    "programming concepts, design principles, and the relevant methodologies that "
    "underpin the work ahead. Setting up version control with Git and GitHub was "
    "treated as a critical skill: it enables tracking changes, collaborating with "
    "team members, and maintaining a professional portfolio of work. The first "
    "milestone — a simple Hello World project — was created to verify that the entire "
    "setup is working correctly, from editor through interpreter to version "
    "control.\n\n"
    "Throughout the phase, team workflows and communication protocols were "
    "understood, including how to interact with mentors and peers. Comprehensive "
    "documentation and curated learning resources tailored to the specialization "
    "were reviewed, and initial onboarding tasks were completed to get familiar with "
    "the tools, processes, and team expectations. By the end of this phase, the "
    "environment is fully configured and a solid foundation is in place for more "
    "advanced work in subsequent phases."
)
doc.add_paragraph(description)

doc.add_paragraph()
doc.add_paragraph(
    "GitHub project URL (optional): https://github.com/username/project"
)

out = "Fundamentals_and_Setup_Report.docx"
doc.save(out)
print("saved", out)