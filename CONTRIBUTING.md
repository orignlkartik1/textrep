# Contributing to textrep

Thank you for your interest in contributing to textrep! We welcome contributions from everyone. This document provides guidelines and instructions for contributing.

## Code of Conduct

This project adheres to the Contributor Covenant [Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots and animated GIFs if possible**
- **Include your Python version and OS**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and expected behavior**
- **Explain why this enhancement would be useful**

### Pull Requests

- Fill in the required template
- Follow the Python style guide
- Include appropriate test cases
- Update documentation as needed
- End all files with a newline
- Avoid platform-dependent code

## Development Setup

### Prerequisites

- Python >= 3.10
- uv (recommended) or pip
- pytest for running tests

### Setting Up Your Development Environment

1. Fork the repository on GitHub
2. Clone your forked repository:
   ```bash
   git clone https://github.com/your-username/textrep.git
   cd textrep
   ```

3. Create a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. Install the package in development mode:
   ```bash
   uv pip install -e ".[dev]"
   ```

### Running Tests

```bash
pytest
```

For coverage report:

```bash
pytest --cov=src/textrep
```

### Code Style

We follow PEP 8 guidelines. Please ensure your code adheres to:

- Line length: 100 characters (soft limit)
- Use type hints where possible
- Use docstrings for modules, classes, and functions

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Pull Request Process

1. Update the README.md with details of changes to the interface
2. Update the CHANGELOG.md with a note on your changes
3. Increase version numbers in setup.py and pyproject.toml following [Semantic Versioning](https://semver.org/)
4. Ensure all tests pass and add new tests for new functionality
5. Request a review from maintainers

## Styleguides

### Python Styleguide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints
- Write docstrings for all public modules, functions, classes, and methods

Example:

```python
def add(a: int, b: int) -> int:
    """
    Add two integers.
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        The sum of a and b
    """
    return a + b
```

### Documentation Styleguide

- Use Markdown
- Reference other sections with relative links
- Include code examples where relevant

## Additional Notes

### Issue and Pull Request Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

## Recognition

Contributors will be recognized in:
- The README.md file
- Release notes for their contributions

## Questions?

Feel free to open an issue with the label `question` or contact the maintainers directly.

Thank you for contributing! 🎉
