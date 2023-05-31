# Cython Project Template

This repository provides a template for a Python package with Cython-based C extensions in a structured directory layout. It also includes useful commands in a Makefile and packaging options to create an installable package. It is designed to help you quickly set up a Python project with C extensions and streamline the development and distribution process.

## Getting Started

To get started with this template:
1. Download source files or clone the repository:

```bash
git clone https://github.com/Ryen-042/Cython-Project-Template.git
```

2. Modify the packages in the `src` directory. Remove example C extensions and add new ones as you need. Also, remove the `Images` and `SFX` if you want add any other files and directories you need.
3. Customize the `setup.py`, `setup.cfg`, and `requirements.txt` files with your project's metadata and dependencies. Make sure to update the Makefile commands where needed.
4. Optionally, update the .flake8 and .ruff.toml files according to your preferences.
5. Use the provided Makefile commands to compile, clean, lint, install, and package your project as you like.

## Project Structure

The project structure follows the recommended [Python Packaging User Guide](https://packaging.python.org/guides/packaging-namespace-packages/) for namespace packages. The `src` directory contains the top-level namespace package, which can be further divided into sub-packages as needed. The project has the following structure:

```bash
.
├── .flake8
├── .gitignore
├── .ruff.toml
├── LICENSE.txt
├── Makefile
├── MANIFEST.in
├── README.md
├── requirements.txt
├── setup.cfg
├── setup.py
└── src
    ├── __main__.py
    ├── extensions
    │   ├── __init__.py
    │   ├── optimizedPrimeFinder
    │   │   ├── optimizedPrimeFinder.pyi
    │   │   ├── optimizedPrimeFinder.pyx
    │   │   └── __init__.py
    │   └── primeFinder
    │       ├── primeFinder.py
    │       └── __init__.py
    ├── Images
    └── SFX
        └── jobs_done.wav
```
The `src` directory contains the project source code and related files. It includes the main entry point file (`__main__.py`) and subdirectories for different C extensions (`extensions`), images (`Images`), and sound effects (`SFX`).

## Makefile Commands

The Makefile contains several useful commands for compiling, packaging, cleaning, linting, and installing the project.

### Compile Cython Code

```bash
make compile
```

This command compiles all Cython `.pyx` files in the `src/extensions` directory into corresponding `.c` and `.pyd` files.

### Force Recompilation

```bash
make compile-force
```

This command forces the recompilation of all Cython `.pyx` files in the `src/extensions` directory into corresponding `.c` and `.pyd` files, regardless of modification times and source code changes.

### Clean Up Build Files

```bash
make clean-build
```

This command removes all build-related directories, including `build`, `dist`, and `[ProjectName].egg-info`.

### Clean Up Compiled Files

```bash
make clean
```

This command executes `clean-build` at the begining, then removes all compiled `.pyd` and `.c` files in the `src/extensions` directory.

### Installing the package

```bash
make install
```

This command uninstalls any existing versions of the package and installs the current version.

### Publish to PyPI

```bash
make publish-pypi
```

This command packages and uploads the project to PyPI.

### Lint Python Files

```bash
make flake8
```

This command lints all Python files in the project using Flake8.

### Lint Cython Files

```bash
make cython-lint
```

This command lints all Cython files in the `src/extensions` directory using Cython-lint.

### Lint All Files

```bash
make lint
```

This command runs all linting commands: `Ruff`, `Flake8`, and `Cython-lint`.
