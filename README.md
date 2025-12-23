# Python Project

[![Lint](https://github.com/pouralijan/python-project/workflows/Lint/badge.svg)](https://github.com/pouralijan/python-project/actions)
[![Test](https://github.com/pouralijan/python-project/workflows/Test/badge.svg)](https://github.com/pouralijan/python-project/actions)
[![Build](https://github.com/pouralijan/python-project/workflows/Build/badge.svg)](https://github.com/pouralijan/python-project/actions)

A modern Python project template using UV for dependency management, with comprehensive tooling for code quality, testing, and CI/CD.

## Features

- **UV**: Fast Python package installer and resolver
- **Ruff**: Extremely fast Python linter and formatter
- **Pytest**: Testing framework with comprehensive test suite
- **Mypy**: Static type checker
- **Pre-commit**: Git hooks for code quality
- **GitHub Actions**: Automated CI/CD pipelines (lint, test, build)
- **Go-Task**: Command runner for development tasks

## Requirements

- Python 3.8+
- [UV](https://github.com/astral-sh/uv) for dependency management

## Installation

### Install UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Clone and Setup

```bash
git clone https://github.com/pouralijan/python-project.git
cd python-project
```

This installs the package in editable mode along with all development dependencies.

## Usage

Run the main module:

```bash
uv run python -m python_project.main
```

Or use the task runner:

```bash
task run
```

## Development

### Task Runner

This project uses Go-Task for common development tasks:

```bash
task --list  # Show available tasks
task test    # Run tests
task lint    # Run linter
```

### Development Workflow

1. **Install dependencies**: `uv sync --extra dev`

2. **Run pre-commit checks**: `task pre-commit`

3. **Run tests**: `task test`

4. **Lint code**: `task lint`

5. **Format code**: `task format`

6. **Fix linting issues**: `task fix`

7. **Type check**: `task type-check`

### Code Quality

- **Linting**: Ruff checks for code quality issues
- **Formatting**: Ruff formats code automatically
- **Type checking**: Mypy ensures type safety
- **Testing**: Pytest runs the test suite

### Building

Build the package for distribution:

```bash
task build
```

## Project Structure

```
├── src/
│   └── python_project/        # Main package
│       ├── __init__.py
│       └── main.py           # Entry point
├── tests/                     # Test files
│   ├── __init__.py
│   └── test_main.py
├── .github/
│   └── workflows/             # GitHub Actions CI
│       ├── lint.yml
│       ├── test.yml
│       └── build.yml
├── ruff.toml                  # Ruff configuration
├── pytest.ini                 # Pytest configuration
├── Taskfile.yml               # Go-task configuration
├── pyproject.toml             # Project metadata and dependencies
├── .pre-commit-config.yaml    # Pre-commit hooks
└── README.md
```

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
