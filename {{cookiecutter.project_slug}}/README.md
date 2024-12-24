# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Installation

```bash
# Create a virtual environment and activate it
poetry shell

# Install dependencies
poetry install
```

## Development

This project uses:
- [Poetry](https://python-poetry.org/) for dependency management
- [Pytest](https://docs.pytest.org/) for testing
- [Ruff](https://github.com/astral-sh/ruff) for linting and formatting
- [Pyright](https://github.com/microsoft/pyright) for type checking
- [Pre-commit](https://pre-commit.com/) for git hooks

### Setup Development Environment

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Setup pre-commit hooks:
   ```bash
   poetry run pre-commit install
   ```

### Running Tests

```bash
poetry run pytest
```

### Code Quality

```bash
# Format code
poetry run ruff format .

# Lint code
poetry run ruff check .

# Type check
poetry run pyright
```

## License

This project is licensed under the {{cookiecutter.open_source_license}} License.
