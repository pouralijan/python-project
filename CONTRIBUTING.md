# Contributing to Python Project

Thank you for your interest in contributing! This document provides guidelines and information for contributors.

## Development Setup

### Prerequisites

- Python 3.12+
- [UV](https://github.com/astral-sh/uv) for dependency management
- [Go-Task](https://taskfile.dev/) for task running

#### Installing Go-Task

```bash
# Using Go (recommended)
go install github.com/go-task/task/v3/cmd/task@latest

# Or using other methods
# See https://taskfile.dev/installation/
```

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/pouralijan/python-project.git
   cd python-project
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

This project follows the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification for commit messages.

#### Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

#### Types

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc.)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `build`: Changes that affect the build system or external dependencies
- `ci`: Changes to CI configuration files and scripts
- `chore`: Other changes that don't modify src or test files

#### Examples

- `feat: add user authentication`
- `fix: resolve memory leak in data processing`
- `docs: update API documentation`
- `refactor: simplify algorithm in utils.py`

#### Additional Rules

- Use clear, descriptive commit messages
- Start with a verb in imperative mood
- Reference issue numbers when applicable (e.g., `fix: resolve issue #123`)
- Keep the subject line under 50 characters
- Use the body for detailed explanations if needed

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

### Changelog Updates

This project maintains a changelog following the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

#### When to Update

- **Added**: For new features
- **Changed**: For changes in existing functionality
- **Deprecated**: For soon-to-be removed features
- **Removed**: For removed features
- **Fixed**: For bug fixes
- **Security**: For vulnerability fixes

#### How to Update

1. Add entries to the `[Unreleased]` section in `CHANGELOG.md`
2. Use past tense for descriptions (e.g., "Added feature" not "Add feature")
3. Group related changes under appropriate headings
4. Reference issue/PR numbers when applicable

#### Example

```markdown
## [Unreleased]

### Added
- New user authentication feature (#123)

### Fixed
- Memory leak in data processing module (#124)
```

### PR Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Keep PRs focused on a single feature or fix
- Ensure CI passes for all checks
- Update the changelog for user-facing changes

### Review Process

- All PRs require review before merging
- Address review feedback promptly
- Maintain respectful and constructive communication

## Reporting Issues

### Bug Reports

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

Thank you for contributing to Python Project! 🚀
