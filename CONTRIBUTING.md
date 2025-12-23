# Contributing to My Python Project

Thank you for your interest in contributing! This document provides guidelines and information for contributors.

## Development Setup

### Prerequisites

- Python 3.12+
- [UV](https://github.com/astral-sh/uv) for dependency management
- [Go-Task](https://taskfile.dev/) for task running

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/my-python-project.git
   cd my-python-project
   ```

2. **Install dependencies**
   ```bash
   uv sync --extra dev
   ```

3. **Install pre-commit hooks** (optional, but recommended)
   ```bash
   uv run pre-commit install
   ```

## Development Workflow

### Task Runner

Use `task` for common development tasks:

```bash
# Show available tasks
task --list

# Run pre-commit checks
task pre-commit

# Run tests
task test

# Lint code
task lint
```

### Manual Commands

If you prefer running commands directly instead of using tasks:

```bash
# Install dependencies
uv sync --extra dev

# Run tests
uv run pytest

# Lint and format
uv run ruff check .
uv run ruff format .

# Type check
uv run mypy src/

# Build
uv build
```

## Code Style

This project uses:

- **Ruff** for linting and formatting
- **Mypy** for static type checking
- **Black** compatible formatting (via Ruff)

### Code Standards

- Follow PEP 8 style guidelines
- Use type hints for all function parameters and return values
- Write comprehensive docstrings
- Keep functions small and focused
- Use meaningful variable and function names

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb in imperative mood (e.g., "Add feature", "Fix bug")
- Reference issue numbers when applicable

## Testing

### Running Tests

```bash
just test
# or
uv run pytest
```

### Writing Tests

- Write tests for new features and bug fixes
- Use descriptive test names
- Follow the existing test structure in `tests/`
- Aim for good test coverage

### Test Structure

```
tests/
├── __init__.py
├── test_main.py
└── ...
```

## Pull Requests

### Before Submitting

1. **Run all checks**: `just pre-commit` or `task pre-commit`
2. **Ensure tests pass**: `just test` or `task test`
3. **Update documentation** if needed
4. **Add tests** for new functionality

### PR Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Keep PRs focused on a single feature or fix
- Ensure CI passes for all checks

### Review Process

- All PRs require review before merging
- Address review feedback promptly
- Maintain respectful and constructive communication

## Reporting Issues

### Bug Reports

When reporting bugs, please include:

- Python version
- Operating system
- Steps to reproduce
- Expected vs. actual behavior
- Error messages/logs

### Feature Requests

For feature requests, please:

- Describe the problem you're trying to solve
- Explain why the current solution isn't sufficient
- Provide examples of the desired functionality

## Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors

## Getting Help

If you need help:

- Check the [README.md](README.md) for setup and usage instructions
- Search existing issues and discussions
- Ask questions in GitHub discussions or issues

Thank you for contributing to My Python Project! 🚀
