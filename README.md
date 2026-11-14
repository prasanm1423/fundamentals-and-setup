# Fundamentals and Setup — Phase 1 Internship Milestone

## Overview
This repository contains the Phase 1 deliverables for the internship fundamentals track. It demonstrates environment setup, version control with Git/GitHub, basic Java programming, and project organization conventions.

## Project Structure
```
foarge/
├── src/
│   └── com/
│       └── internship/
│           └── hello/
│               └── Greeting.java      # Hello World milestone
├── build/                             # Compiled .class files (gitignored)
├── Fundamentals_and_Setup_Report.docx # Final report
├── make_report.py                     # Report generation script
└── README.md
```

## Prerequisites
- Java SE 8+ (tested on Java 26)
- Git
- Code editor of choice (VS Code, IntelliJ IDEA, etc.)

## Building and Running
```bash
# Compile
javac -d build src/com/internship/hello/Greeting.java

# Run
java -cp build com.internship.hello.Greeting
```

Expected output:
```
Hello, World!
Hello, Internship!
```

## What This Demonstrates
1. **Environment Setup** — Java installation verified
2. **Version Control** — Git initialized, commits made, pushed to GitHub
3. **Project Conventions** — Standard package naming (com.domain.project.module)
4. **Build Process** — Manual compilation demonstrating the concept
5. **Documentation** — README explains setup and usage

## Git Workflow Completed
- Initialized local repository
- Created `.gitignore` for build artifacts
- Made initial commit with all source files
- Linked to remote GitHub repository
- Pushed to master branch

## Next Steps
Move to Phase 2 where more advanced frameworks and larger-scale projects will be introduced.

---
Candidate: Prasa  
Date: 2026-11-14  
Repository: https://github.com/prasanm1423/fundamentals-and-setup
