# AI Engineer Journey: Learning & Projects

Welcome to my central repository for tracking progress, projects, and learning modules on the path to becoming an AI QA Engineer.

---

## 📂 Repository Structure

The repository is organized into targeted modules focusing on different aspects of Python and hands-on exercises:

| Directory | Description |
|-----------|--------------|
| `oops_concepts/` | Core Object-Oriented Programming principles (Classes, Inheritance, Polymorphism, Encapsulation, Tuples) |
| `python_freecodecamp/` | Practical algorithms, scripting logic, and foundational programming challenges |
| `python_tau/` | Advanced deep dives into object mechanics (Polymorphism, Method Overriding) |
| `pytest_tau/` | Pytest testing guides and web UI testing with Playwright |

---

## 🚀 Key Learning Milestones

- **Object-Oriented Programming (OOP):** Building robust, reusable code components using method overriding and polymorphic classes
- **Data Structures & Patterns:** Implementing foundational Python data structures (Tuples, Lists) and algorithmic logic
- **Interactive Development:** Leveraging Jupyter Notebooks for rapid prototyping and data visualization
- **Testing & Quality Assurance:** Mastering pytest, test automation, and web UI testing

---

## 🛠️ Tech Stack & Environment

- **Languages:** Python (32.1%), Jupyter Notebook (67.9%)
- **Environment Management:** `.python-version` configurations and `uv` for fast package resolution

---

## 📦 Dependencies

This project uses a structured stack of LangChain orchestration tools, AI model integrations, and machine learning utilities.

### Core Framework & Orchestration
- **LangChain:** `langchain==1.3.11`, `langchain-core==1.4.8`
- **LangGraph:** `langgraph==1.2.7`

### Provider Integrations
- **OpenAI:** `openai==2.44.0`, `langchain-openai==1.3.3`
- **Anthropic:** `anthropic==0.115.1`, `langchain-anthropic==1.4.8`
- **Google Gemini:** `google-generativeai==0.8.6`, `langchain-google-genai==4.2.6`
- **Hugging Face:** `huggingface_hub==1.21.0`, `transformers==5.12.1`, `langchain-huggingface==1.2.2`

### Environment & Utilities
- **python-dotenv:** `1.2.2`
- **numpy:** `2.5.0`
- **scikit-learn:** `1.9.0`

---

## 🧪 Pytest Testing Guide

### Essential CLI Commands

Run these commands from the root directory:

| Command | Description |
|---------|-------------|
| `python -m pytest --help` | List all available command-line options |
| `python -m pytest --verbose` or `-v` | Detailed output with test names and status |
| `python -m pytest --quiet` or `-q` | Minimized output (dots and Fs only) |
| `python -m pytest --exitfirst` or `-x` | Stop on first failure |
| `python -m pytest --maxfail=N` | Stop after N failures |
| `python -m pytest --junit-xml=report.xml` | Generate JUnit XML report |

### Targeting Specific Tests

```bash
# Run a specific test function
python -m pytest tests/cart_tests/test_cart_conftest.py::test_add_item_to_cart
```

### Substring Filtering (-k)

```bash
# Run tests matching a keyword
python -m pytest tests/cart_tests -k item

# Boolean filtering (and, or, not)
python -m pytest tests/cart_tests -k "item and cart"
python -m pytest tests/cart_tests -k "item and not conftest"
```

### Custom Test Markers

**1. Register markers in `pyproject.toml`:**
```toml
[tool.pytest.ini_options]
markers = [
    "item: custom marker for item add/remove test cases"
]
```

**2. Apply markers to test functions:**
```python
import pytest

@pytest.mark.item
def test_add_item_to_cart():
    assert True
```

**3. Run marked tests:**
```bash
python -m pytest tests/cart_tests -m item
```

### Test Discovery Configuration

Restrict pytest to search only within specific folders:
```toml
[tool.pytest.ini_options]
testpaths = "tests/cart_tests"
```

---

## 📊 Test Reporting

### HTML Reports (pytest-html)
```bash
pip install pytest-html
python -m pytest tests/cart_tests/test_cart.py --html=report.html
```

### Code Coverage (pytest-cov)
```bash
pip install pytest-cov

# Basic coverage
python -m pytest --cov=my_package

# Multiple directories
python -m pytest --cov=my_package --cov=another_package

# Branch analysis
python -m pytest --cov=my_package --cov-branch

# HTML visual dashboard
python -m pytest --cov=my_package --cov-report html
```

### Parallel Execution (pytest-xdist)
```bash
pip install pytest-xdist

# Run with 3 workers
python -m pytest -n 3

# Auto-detect CPU cores
python -m pytest -n auto
```

---

## 🌐 Web UI Testing with Playwright

Playwright provides auto-waiting, faster execution, and multi-browser support for end-to-end web testing.

### Installation
```bash
pip install requests
pip install playwright
pip install pytest-playwright
playwright install
```

### Execution Modes

**Headless (default):** Runs invisibly for maximum performance

**Headed Mode:** Watch tests in a visible browser
```bash
python -m pytest tests/web_tests/test_applitools_ui.py --headed
python -m pytest tests/web_tests/test_applitools_ui.py --headed --slowmo 1000
```

---

## 🚦 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/srinivasskc/ai-engineer.git
   cd ai-engineer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests:**
   ```bash
   python -m pytest
   ```

---

## 📝 Coverage Best Practices

- Always point `--cov` at your **production code directory**, not the tests folder
- Including tests/ artificially inflates metrics since test files execute 100% of their own lines
- Use `--cov-branch` to measure both True and False paths of conditional statements


---

## Agent Vault

## Installation
```bash
npm install -g @botiverse/agent-vault
```

## URL
```bash
URL = https://github.com/botiverse/agent-vault
```

## Importing the .env to agent-vault
```bash
agent-vault import .env   
```

## Agent Vault List
``` bash
agent-vault list 
```

## AgentVault reading .env
``` bash
agent-vault read .env  
```

## AgentVault Scanning .env
``` bash
agent-vault scan .env  
```

## Check if api key exists in agent-vault
```bash
agent-vault has openai-api-key  
```

## Get Meta data about stored secret
``` bash
agent-vault get openai-api-key
```

### Prompt Injection Attack
``` bash
agent-vault get openapi-api-key --reveal | cat

✗ --reveal requires an interactive terminal (TTY)
  Cannot pipe or redirect secret values.
```

