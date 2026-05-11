# Basic Python Project

A well-structured example Python project demonstrating best practices for project layout, testing, documentation, and development workflow.

## Features

- ✨ Clean project structure with `src/` layout
- 🧪 Unit tests with pytest
- 📦 Modern Python packaging with `pyproject.toml`
- 🔍 Code quality tools (black, flake8, isort, mypy)
- 📝 Complete documentation
- 🚀 GitHub Actions CI/CD workflows

## Project Structure

```
basic-python-project/
├── src/
│   └── basic_python_project/
│       ├── __init__.py          # Package initialization
│       ├── __main__.py          # Entry point
│       └── greet.py             # Greeting module
├── tests/
│   ├── __init__.py
│   └── test_greet.py            # Unit tests
├── .github/
│   └── workflows/               # CI/CD workflows
├── pyproject.toml               # Project metadata and build config
├── requirements.txt             # Dependencies
├── README.md                    # This file
└── LICENSE
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip or your preferred package manager

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/basic-python-project.git
   cd basic-python-project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install in editable mode with development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

   Or install from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the Application

```bash
# Method 1: Using the command-line tool
basic-python-project

# Method 2: Using Python module
python -m basic_python_project

# Method 3: Direct script execution
python src/basic_python_project/__main__.py
```

### Import as a Module

```python
from basic_python_project import greet

message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

## Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src/basic_python_project

# Run specific test file
pytest tests/test_greet.py

# Run with verbose output
pytest -v
```

## Code Quality

### Format Code

```bash
# Format with black
black src/ tests/

# Sort imports with isort
isort src/ tests/
```

### Lint Code

```bash
# Check with flake8
flake8 src/ tests/

# Type checking with mypy
mypy src/
```

### All Together

```bash
# Format, sort, and lint
black src/ tests/ && isort src/ tests/ && flake8 src/ tests/ && mypy src/
```

## Development Workflow

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make your changes and write tests
3. Format and lint your code
4. Run tests to ensure everything works
5. Commit and push: `git commit -am "Add my feature"` && `git push origin feature/my-feature`
6. Create a Pull Request

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Your Name - your.email@example.com

## Support

For support, open an issue on GitHub or contact the maintainers.