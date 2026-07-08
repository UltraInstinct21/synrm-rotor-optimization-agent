---
type: motorcad_development
title: "Contributing to PyMotorCAD"
source: "PyMotorCAD Documentation"
tags:
  - motorcad
  - pymotorcad
  - contributing
  - development
  - testing
  - documentation
aliases:
  - "PyMotorCAD development setup"
  - "PyMotorCAD contribution guide"
---

# Contributing to PyMotorCAD

## Overview

PyMotorCAD is an open-source Python package maintained by Ansys for scripting Motor-CAD motor design workflows. Contributions — bug reports, feature requests, documentation improvements, and code — are accepted through the public GitHub repository.

---

## Installation

### End Users

Install the latest stable release from PyPI:

```powershell
pip install ansys-motorcad-core
```

### Developers (Editable Install)

Clone the repository and install in editable mode to work on the source code directly:

```powershell
git clone https://github.com/ansys/pymotorcad.git
cd pymotorcad
pip install -e ".[dev]"
```

The editable install links the local source to your Python environment so code changes take effect immediately without reinstalling.

---

## Development Environment Setup

### System Requirements

- Python 3.9+ (3.11+ recommended)
- Git
- Motor-CAD installed and licensed (for running integration tests)
- tox (installed automatically with dev dependencies)

### Virtual Environment (Recommended)

Create a dedicated development venv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

This installs all dependencies for building, testing, and documenting PyMotorCAD.

---

## Code Style and Linting

PyMotorCAD enforces consistent code style through automated tooling.

### Style Rules

- PEP 8 compliance (enforced via `ruff`)
- Type annotations required on public API methods
- Docstrings follow NumPy convention
- Maximum line length: 100 characters

### Running the Style Check

```powershell
tox -e style
```

This runs linting and formatting checks across the entire codebase. All checks must pass before submitting a pull request.

### Pre-commit Hooks

Install pre-commit hooks to catch style issues locally before committing:

```powershell
pre-commit install
```

After installation, hooks run automatically on each `git commit`. To run hooks manually on all files:

```powershell
pre-commit run --all-files
```

The pre-commit configuration includes:

- Trailing whitespace removal
- End-of-file fixer
- YAML validation
- Ruff linting and formatting
- Ruff import sorting

---

## Running Tests

PyMotorCAD uses `tox` to manage isolated test environments. All test commands are run from the repository root.

### Unit Tests (No Motor-CAD Required)

```powershell
tox -e py
```

Runs the full unit test suite using pytest. These tests do not require a Motor-CAD installation and mock external dependencies.

### Test Coverage

```powershell
tox -e py-coverage
```

Generates a test coverage report. Coverage thresholds are enforced — pull requests that reduce coverage below the configured minimum will fail CI.

### Full Test Suite

```powershell
tox
```

Running `tox` without specifying an environment executes all defined environments in sequence: style checks, unit tests, and documentation builds.

### Writing Tests

- Tests are located in the `tests/` directory
- Unit tests mock the Motor-CAD connection; integration tests (when available) require a live Motor-CAD instance
- Use descriptive test names that explain the expected behavior
- Each test should verify one behavior
- Use `pytest.raises` for expected exceptions

Example test structure:

```python
import pytest
import ansys.motorcad.core as pymotorcad

def test_motorcad_connection():
    """Test that Motor-CAD instance can be created."""
    # This test uses mocked connections
    mc = pymotorcad.MotorCAD(open_new_instance=False)
    assert mc is not None

def test_set_variable():
    """Test setting a Motor-CAD variable."""
    mc = pymotorcad.MotorCAD(open_new_instance=False)
    mc.set_variable("Airgap", 0.5)
    assert mc.get_variable("Airgap") == 0.5
```

---

## Documentation

### Build Documentation Locally

PyMotorCAD uses Sphinx to generate documentation. Build the docs locally with:

```powershell
tox -e doc
```

This generates HTML documentation in the `doc/_build/html/` directory.

### Documentation Structure

- API reference is auto-generated from docstrings
- User guide pages are written in reStructuredText (`.rst`)
- Code examples live in the `examples/` directory
- Each public method must have a complete NumPy-style docstring

### Docstring Convention

```python
def set_variable(self, variable_name: str, value: float | int | str) -> None:
    """Set a Motor-CAD variable.

    Parameters
    ----------
    variable_name : str
        Name of the Motor-CAD variable to set.
    value : float | int | str
        Value to assign to the variable.

    Raises
    ------
    ValueError
        If the variable name is not recognized.

    Examples
    --------
    >>> mc.set_variable("Airgap", 0.5)
    >>> mc.set_variable("Pole_Number", 4)
    """
```

---

## Pull Request Workflow

### 1. Fork and Clone

Fork the repository on GitHub, then clone your fork:

```powershell
git clone https://github.com/<your-username>/pymotorcad.git
cd pymotorcad
```

### 2. Create a Feature Branch

```powershell
git checkout -b feature/my-feature-name
```

### 3. Make Changes and Test

- Write code following the style guide
- Add or update tests for new functionality
- Run the full test suite: `tox`
- Ensure all checks pass

### 4. Commit

Write clear, descriptive commit messages:

```powershell
git add .
git commit -m "Add motor parameter validation for SynRM barrier geometry"
```

### 5. Push and Create Pull Request

```powershell
git push origin feature/my-feature-name
```

Open a pull request on GitHub against the `main` branch. The PR description should include:

- What the change does and why
- Any Motor-CAD version requirements
- Test results or screenshots if applicable
- Breaking changes, if any

### 6. Code Review

Maintainers will review the PR. Address feedback by pushing additional commits. The PR is merged once all CI checks pass and at least one maintainer approves.

---

## Reporting Issues

### Bug Reports

Open an issue on GitHub with:

- PyMotorCAD version (`pip show ansys-motorcad-core`)
- Motor-CAD version
- Python version
- Operating system
- Minimal code to reproduce the issue
- Full error traceback

### Feature Requests

Open an issue describing:

- The use case
- Current workaround, if any
- Proposed API or behavior

---

## Project Structure

```
pymotorcad/
├── src/
│   └── ansys/
│       └── motorcad/
│           └── core/
│               ├── __init__.py
│               ├── motorcad.py          # Main MotorCAD class
│               ├── _rcodes.py           # Motor-CAD RCode mappings
│               ├── _exceptions.py       # Custom exception classes
│               └── _internal/           # Internal utility modules
├── tests/
│   ├── test_motorcad.py
│   └── test_*.py
├── examples/
│   └── *.py
├── doc/
│   ├── conf.py
│   └── src/
├── tox.ini
├── pyproject.toml
├── .pre-commit-config.yaml
└── README.md
```

---

## Versioning

PyMotorCAD follows Semantic Versioning (SemVer):

- **MAJOR** — breaking API changes
- **MINOR** — new features, backward-compatible
- **PATCH** — bug fixes, backward-compatible

Check the current version:

```python
import ansys.motorcad.core
print(ansys.motorcad.core.__version__)
```

---

## Related Pages

- [[pymotorcad-getting-started]] — First steps with PyMotorCAD
- [[pymotorcad-virtual-environment]] — Configure custom Python venv
- [[motorcad_api/index]] — PyMotorCAD API reference
- [[motorcad_workflows/index]] — Motor-CAD workflow guides
