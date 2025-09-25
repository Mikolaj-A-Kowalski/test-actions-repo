# Hello World Project

A simple Python "Hello World" project demonstrating modern Python packaging with `pyproject.toml` and GitHub Actions CI/CD.

## Features

- Modern Python packaging with `pyproject.toml`
- Command-line interface
- Automated testing with pytest
- Code formatting with Black and isort
- Linting with flake8
- GitHub Actions CI/CD pipeline

## Installation

### From source

```bash
git clone https://github.com/yourusername/hello-world-project.git
cd hello-world-project
pip install -e .
```

### Development installation

```bash
git clone https://github.com/yourusername/hello-world-project.git
cd hello-world-project
pip install -e ".[dev]"
```

## Usage

After installation, you can run the hello world command:

```bash
hello-world
```

Or use it as a Python module:

```python
from hello_world import greet

print(greet("World"))
```

## Development

### Running tests

```bash
pytest
```

### Code formatting

```bash
black .
isort .
```

### Linting

```bash
flake8
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
