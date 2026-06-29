# AI Engineer Journey: Learning & Core Python

Welcome to my central repository for tracking my progress, projects, and learning modules on the path to becoming an AI QA Engineer. 
---

## 📂 Repository Structure

The repository is organized into targeted modules focusing on different aspects of Python and hands-on exercises:

* **`oops_concepts/`**: Focuses on core Object-Oriented Programming principles in Python (Classes, Inheritance, Polymorphism, Encapsulation, and data structures like Tuples).
* **`python_freecodecamp/`**: Practical algorithms, scripting logic, and foundational programming challenges (e.g., number pattern generators).
* **`python_tau/`**: Advanced deep dives into object mechanics, specifically showcasing concepts like **Polymorphism** and **Method Overriding**.

---

## 🚀 Key Learning Milestones

* **Object-Oriented Programming (OOP):** Mastered building robust, reusable code components using method overriding and polymorphic classes.
* **Data Structures & Patterns:** Implementing foundational Python data structures (Tuples, Lists) and algorithmic logic.
* **Interactive Development:** Leveraging Jupyter Notebooks for rapid prototyping and clean data visualization.

---

## 🛠️ Tech Stack & Environment

* **Languages:** Python (32.1%), Jupyter Notebook (67.9%)
* **Environment Management:** Managed seamlessly via `.python-version` configurations and `uv` for fast package resolution.

### Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/srinivasskc/ai-engineer.git](https://github.com/srinivasskc/ai-engineer.git)
   cd ai-engineer

# Pytest Cheat Sheet: Commands & Configs

This repository demonstrates essential command-line options and configuration techniques for optimizing test execution using `pytest`.

---

## 🚀 Essential CLI Commands

Run these commands from the root directory of your project to control test output and execution behavior.

### 1. Help Menu
List all available command-line options, descriptions, and active plugin flags.
```bash
python -m pytest --help
```

###  2. Verbose Output (-v / --verbose)
Prints a highly detailed console output displaying metadata, the full path, explicit name, and individual status (PASSED/FAILED) for each test case.
```bash
python -m pytest tests/test_math.py --verbose
```

###  3. Quiet Mode (-q / --quiet)
Minimizes console noise by hiding the initialization banner and module paths. It prints only the foundational progress indicators (dots and Fs) followed by failure introspections.
```bash
python -m pytest tests/test_math.py --quiet
```

###  4. Exit First (-x / --exitfirst)
Instructs pytest to instantly halt the entire test suite execution the moment a single failure is encountered.
```bash
python -m pytest tests/test_math.py --exitfirst
```

###  5. Maximum Failures (--maxfail)
Stops test execution completely after reaching a specific threshold of failures. This is highly efficient for managing large-scale test suites.
```bash
python -m pytest tests/test_math.py --maxfail=1
```

###  6. Generate JUnit XML Reports (--junit-xml)
Exports test results into a standard JUnit XML report format (report.xml), which is widely compatible with Continuous Integration (CI) dashboards like Jenkins or GitHub Actions.
```bash
python -m pytest tests/test_math.py --junit-xml report.xml
```


