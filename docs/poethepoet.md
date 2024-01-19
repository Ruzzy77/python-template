# Poe the Poet (poe)

## Table of Contents

- [Poe the Poet (poe)](#poe-the-poet-poe)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [poe cli options](#poe-cli-options)
  - [Tasks](#tasks)
    - [workspace](#workspace)
    - [formatter](#formatter)
    - [black](#black)
    - [isort](#isort)
    - [pydocstyle](#pydocstyle)
    - [docformatter](#docformatter)
    - [clean](#clean)
    - [build](#build)
    - [update](#update)
    - [test](#test)

## Description

Poe the Poet is a batteries included task runner that works well with poetry.

It provides a simple way to define project tasks within your pyproject.toml, and either a standalone CLI or a poetry plugin to run them using your project’s virtual environment.

“Simple things should be simple, complex things should be possible.” – Alan Kay

[![GitHub repo](https://img.shields.io/github/stars/nat-n/poethepoet?style=social)](https://github.com/nat-n/poethepoet)
[![PyPI - Python](https://img.shields.io/pypi/pyversions/poethepoet.svg)](https://pypi.org/project/poethepoet/)
[![PyPI - Version](https://img.shields.io/pypi/v/poethepoet.svg)](https://pypi.org/project/poethepoet/)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/poethepoet)](https://pypistats.org/packages/poethepoet)
[![License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/nat-n/poethepoet/blob/main/LICENSE)

[Documentation](https://poethepoet.natn.io)

## poe cli options

```bash
poe --help
poe --quiet     # decrease poe's internal output
poe -qq         # decrease verbosity (repeatable)
poe --verbose   # increase poe's internal output
poe -vv         # increase verbosity (repeatable)
```

## Tasks

> Note: Each header is a task name.

### workspace

- Print current workspace

  > $WORKSPACE is defined in pyproject.toml/[tool.poe] section.

  ```bash
  poe workspace
  ```

### formatter

> Run black, isort, docformatter.

```bash
poe format [-v,--verbose] [-q,--quiet] [targets... (default: .)]
```

- Example

  > `-q,--quiet` option is useful when you want to run formatter in CI.  
  > `--` is used to separate poe options and black/isort options.

  ```bash
  poe format
  poe -q format .
  poe -q format src tests   # targets must be exist in pwd
  ```

### black

> The uncompromising Python code formatter.

```bash
poe black [-v,--verbose] [targets... (default: .)]
```

### isort

> Sort imports alphabetically, and automatically separated into sections and by type.

```bash
poe isort [-v,--verbose] [targets... (default: .)]
```

### pydocstyle

> Check docstring style conventions.

```bash
poe pydocstyle [-v,--verbose] [targets... (default: .)]
```

### docformatter

> Formats docstrings to follow PEP 257.  
> --check, --in-place are mutually exclusive. don't use both.

```bash
poe docformatter [-d,--diff] [-c,--check] [-i,--in-place] [targets... (default: .)]
```

### clean

> Remove temporary files. <i>(\_\_pycache\_\_, .pytest_cache, .coverage, .mypy_cache, .tox, .eggs, dist, build, \*.egg-info, .ipynb_checkpoints, .DS_Store)</i>

```bash
poe clean [-v,--verbose] [-d,--dry-run] [targets... (default: .)]
```

### build

> Build package.

```bash
poe build
```

### update

> Update package with poetry.

```bash
poe update
```

### test

> Run tests with pytest.  
> <i>Note: --collect_only, --no_cov are use underscore instead of dash. (poe argparse limitation)</i>

```bash
poe test [-v,--verbose] [-co,--collect_only] [-n,--no_cov] [targets... (default: .)]
```
