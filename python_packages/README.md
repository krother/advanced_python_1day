
# Build a Python Package

In this exercise, you will use  `uv <https://docs.astral.sh/uv/>`__ to package the `space` application.
**uv** is a modern tool for managing virtual environments written in rust. It works similar to **pipenv** and **poetry** but is 100x faster when resolving dependencies.

While inspecting the code, make sure to discuss the following questions:

- what is a namespace?
- monkey patching
- what is reference counting?
- what are modules / packages / libraries?
- what are absolute and relative imports?
- how does Python find modules?
- what to use `__init__.py` for
- where to keep custom exceptions?
- how to define a custom logger?
- what is a namespace package?

## 1. Installation

Install uv with:

    python -m pip install uv

or

    curl -LsSf https://astral.sh/uv/install.sh | sh


## 2. Create environment

Execute the commands

    uv python install 3.12
    uv init

## 3. pyproject.toml

The file `pyproject.toml` creates everything to package the project.
Inspect the file and clarify its contents.

## 4. Install libraries

Install the dependencies listed in `pyproject.toml`:

    uv lock
    uv sync

The development libraries are installed by default.

## 5. Execute code

Now the program is ready to be executed.
There are multiple options:

    uv run python space_game
    uv run python space_game gui

Also using the `[project.scripts]` configuration:

    uv run space
    uv run space_gui

## 6. Release the package

Create a distribution with:

    uv build

You should find the release files in the `dist/` folder.

If you want to release the sources only, use:

    uv build --sdist

## 7. Install the package

The newly created package can be installed with ``pip`` from the release wheel:

    pip install dist/pandas_go_to_space-1.1.0-py3-none-any.whl

and

    python
    
    >>> import space_game

## 8. Code checks

in [code_checks.md](code_checks.md) you find a couple of tools to inspect your code.

## Links

- [uv Tutorial](https://python-basics-tutorial.readthedocs.io/en/latest/libs/distribution.html#uv)
- [Modules](https://python-basics-tutorial.readthedocs.io/en/latest/modules/index.html)
- [Libraries](https://python-basics-tutorial.readthedocs.io/en/latest/libs/index.html)
- [Logging](https://www.academis.eu/advanced_python/error_handling/logging.html)
- [Packaging](https://python-basics-tutorial.readthedocs.io/en/latest/packs/index.html)
- [Namespace Packages](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/)
