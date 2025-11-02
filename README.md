# Ciphr

A Python port of [frohoff/ciphr](https://github.com/frohoff/ciphr), a CLI tool for encoding, decoding, hashing, and cryptographic operations on streams.

## Status
Work in progress. Currently in the initial setup phase.

## Development Setup

### Prerequisites

- Python 3.10 or later
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

### Setting up the development environment

1. Clone the repository:
   ```sh
   git clone https://github.com/hyonsoku/ciphr.git
   cd ciphr
   ```

2. Create and activate a virtual environment with uv:
   ```sh
   uv venv
   # On Windows PowerShell:
   .venv/Scripts/Activate.ps1
   # On Unix-like systems:
   # source .venv/bin/activate
   ```

3. Install the package in development mode with all dev dependencies:
   ```sh
   uv pip install -e ".[dev]"
   ```

### Running Tests

Run the test suite using pytest:
```sh
pytest tests/ -v
```

### Updating Dependencies

To update your development environment:

1. Update all dependencies to their latest compatible versions:
   ```sh
   # First, upgrade uv itself if needed
   pip install --upgrade uv

   # Update all dependencies
   uv pip install --upgrade -e ".[dev]"
   ```

2. View outdated packages:
   ```sh
   uv pip list --outdated
   ```

3. Update specific packages:
   ```sh
   uv pip install --upgrade package-name
   ```

4. Generate requirements files (optional):
   ```sh
   uv pip freeze > requirements.txt
   uv pip freeze --dev > requirements-dev.txt
   ```

5. Synchronize environment with requirements files (optional):
   ```sh
   # If you have requirements.txt
   uv pip sync requirements.txt requirements-dev.txt
   ```

### Code Style

The code follows the black code style. To format your code:
```sh
black src/ tests/
```

To check code quality with flake8:
```sh
flake8 src/ tests/
```

## Documentation

- [Specification](docs/specification.yaml): Detailed specification of Ciphr's features and behavior, including CLI input/output details.
- [Installation](docs/installation.md): How to install Ciphr.
- [Examples](docs/examples.md): Usage examples

## License
MIT License. See [LICENSE](LICENSE) for details.

## Credits
Original Ruby implementation by [frohoff](https://github.com/frohoff/ciphr)