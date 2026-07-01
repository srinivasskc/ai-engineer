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

# Pytest Cheat Sheet: Filtering and Syntax Rules

When running specific tests in a project, matching `pytest`'s precise syntax is crucial. This guide clarifies how to target individual test functions within a specific test module.

---

## 🔍 Targeting Specific Tests

### Syntax (Double Colon)
```bash
python -m pytest tests/cart_tests/test_cart_conftest.py::test_add_item_to_cart
```


---

## 🏷️ Substring Filtering (`-k`)

You can run a specific subset of tests across files and directories by matching keywords in their function names using the `-k` flag.

### Run tests matching a specific keyword
To execute all tests that contain the word `item` in their function name within a target directory:
```bash
python -m pytest tests/cart_tests -k item
```

### Advanced Boolean Filtering
The -k flag supports boolean logic (and, or, not), allowing you to combine or exclude specific terms dynamically:

Match multiple terms: Run tests containing both item AND cart:
```bash
python -m pytest tests/cart_tests -k "item and cart"
```

Exclude terms: Run tests containing item but NOT conftest:
```bash
python -m pytest tests/cart_tests -k "item and not conftest"
```

## Custom Markers
To add your custom markers using pyproject.toml, you need to register them under the [tool.pytest.ini_options] block using the markers configuration option.

---

## 🏷️ Custom Test Markers (`markers`)

Custom markers allow you to tag specific test cases so you can run them selectively as a group.

### 1. Registering Markers in `pyproject.toml`
To avoid unexpected configuration warnings, always register your custom markers in your `pyproject.toml` file under the `[tool.pytest.ini_options]` block using an array:

```toml
[tool.pytest.ini_options]
addopts = "--verbose"
markers = [
    "item: custom marker for item add/remove test cases"
]
```

### 2. Applying Markers to Code
Decorate your test functions using @pytest.mark.<marker_name>:
```  Python
import pytest

@pytest.mark.item
def test_add_item_to_cart():
    assert True
```

### 3. Running Marked Tests (-m)
To execute only the test cases tagged with your custom marker, use the -m flag:

```Bash
python -m pytest tests/cart_tests -m item
```

### 4. Include Only Specific Patterns
To execute tests matching a keyword *only* if they also appear within a specific file pattern or configuration context (such as a local `conftest` directory setup):
```bash
python -m pytest tests/cart_tests -k "item and conftest"
```

---

## 5. Restricting Test Discovery (`testpaths`)

By default, pytest searches your entire workspace directory to discover tests. For large projects, this can slow down discovery times.

### 6. Enforcing Search Directories in `pyproject.toml`
To optimize discovery and restrict pytest to search *only* within a specific folder, use the `testpaths` configuration option:

```toml
[tool.pytest.ini_options]
addopts = "--verbose"
markers = [
    "item: custom marker for item add/remove test cases"
]
testpaths = "tests/cart_tests"
```


### 7. Test Reporting
Extend your local test architecture with metrics and shareable reporting frameworks.

HTML Test Reports (pytest-html)
Generates a permanent, shareable standalone HTML document summarizing your test run.

```Bash
pip install pytest-html
python -m pytest tests/cart_tests/test_cart.py --html=report.html
```


### 8. Code Coverage Tracking (pytest-cov)
Integrates coverage.py to calculate what percentage of your source code is verified by your test suite.

```Bash
pip install pytest-cov
```

### Critical Coverage Best Practices:
Target Product Code Only: Always point the --cov flag at your actual production code directory, not your tests folder. Including the tests/ directory artificially inflates metrics since test files naturally execute 100% of their own lines during discovery.

```Bash
python -m pytest --cov=my_package
```

### Tracking Multiple Directories: 
To aggregate coverage metrics across multiple package roots into a unified report, pass individual flags side-by-side:

```Bash
python -m pytest --cov=my_package --cov=another_package
```

### Advanced Coverage Configurations
Branch Analysis (--cov-branch): Forces the coverage engine to measure logical pathing (evaluating both the True and False outcomes of a conditional if/else block) rather than just tracking line execution. Highly recommended as a baseline suite option.

```Bash
python -m pytest --cov=my_package --cov-branch
```

### Visual HTML Dashboards (--cov-report html): 
Generates an interactive, line-by-line visual report inside a generated htmlcov/ folder. Open htmlcov/index.html in any browser to see code paths highlighted in green (covered) or red (missed statement gaps).

```Bash
python -m pytest --cov=my_package --cov-report html
```

### 9. Parallel Execution Scaling (pytest-xdist)
Scale your execution speed by distributing your test workloads across multiple CPU cores instead of running them sequentially.

```Bash
pip install pytest-xdist
```

### Parallel Execution Commands
Specify the exact number of worker processes to allocate via the -n flag:

```Bash
python -m pytest -n 3
```

### Auto-Scale Mode: 
Instructs pytest to auto-detect and utilize every logical core available on your local runtime architecture:

```Bash
python -m pytest -n auto
```
