# Poetry Installation

## Installation

### Linux / macOS / Windows

```bash
$ curl -sSL https://install.python-poetry.org | python3 -
```

### Windows (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### Install result

```bash
Retrieving Poetry metadata

# Welcome to Poetry!

This will download and install the latest version of Poetry,
a dependency and package manager for Python.

It will add the `poetry` command to Poetry's bin directory, located at:

/home/user/.local/bin

You can uninstall at any time by executing this script with the --uninstall option,
and these changes will be reverted.

Installing Poetry (1.5.1): Done

Poetry (1.5.1) is installed now. Great!

To get started you need Poetry's bin directory (/home/user/.local/bin) in your `PATH`
environment variable.

Add `export PATH="/home/user/.local/bin:$PATH"` to your shell configuration file.

Alternatively, you can call Poetry explicitly with `/home/user/.local/bin/poetry`.

You can test that everything is set up by executing:

`poetry --version`

```

### After installation

-   Add `export PATH="/home/user/.local/bin:$PATH"` to your shell configuration file.

    -   bash

        ```bash
        $ echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
        $ source ~/.bashrc
        ```

    -   zsh
        ```bash
        $ echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
        $ source ~/.zshrc
        ```

### Enable tab completion

-   bash
    ```bash
    $ poetry completions bash > ~/.bash-completion
    ```
-   zsh
    ```bash
    $ poetry completions zsh > ~/.zfunc/_poetry
    ```
-   oh-my-zsh
    ```bash
    $ mkdir $ZSH_CUSTOM/plugins/poetry
    $ poetry completions zsh > ~/.oh-my-zsh/custom/plugins/poetry/_poetry
    ```
    you must then add `poetry` to the plugins array in your `.zshrc` file.

    ```bash
    plugins(
        poetry
        ...
	)
    ```

<br/><br/>

## How to use

### Update

```bash
$ poetry self update
$ poetry self update --preview
$ poetry self update 1.2.0
```

### Install dependencies

```bash
$ poetry install
```


### Add dependencies

```bash
$ poetry add <package>
$ poetry add <package> --dev
$ poetry add <package> --optional
$ poetry add <package> --dry-run
$ poetry add <package> --lock
$ poetry add <package> --lock --dry-run
```

### Remove dependencies

```bash
$ poetry remove <package>
$ poetry remove <package> --dev
$ poetry remove <package> --dry-run
$ poetry remove <package> --lock
$ poetry remove <package> --lock --dry-run
```

### Update dependencies

```bash
$ poetry update
$ poetry update <package>
$ poetry update <package> <package>
$ poetry update <package> --dry-run
$ poetry update <package> --lock
$ poetry update <package> --lock --dry-run
```

### Show dependencies

```bash
$ poetry show
$ poetry show <package>
$ poetry show --tree
$ poetry show --latest
$ poetry show --outdated
$ poetry show --no-dev
$ poetry show --no-dev --tree
$ poetry show --no-dev --latest
$ poetry show --no-dev --outdated
```

### Show dependency information

```bash
$ poetry show --info <package>
$ poetry show --info <package> <package>
$ poetry show --info --tree <package>
$ poetry show --info --latest <package>
$ poetry show --info --outdated <package>
$ poetry show --info --no-dev <package>
$ poetry show --info --no-dev --tree <package>
$ poetry show --info --no-dev --latest <package>
$ poetry show --info --no-dev --outdated <package>
```

### Show dependency versions

```bash
$ poetry show --no-dev --tree --latest
$ poetry show --no-dev --tree --outdated
```

### Show dependency vulnerabilities

```bash
$ poetry show --latest --no-dev --tree --vulnerabilities
$ poetry show --outdated --no-dev --tree --vulnerabilities
```

### Show dependency licenses

```bash
$ poetry show --no-dev --tree --latest --licenses
$ poetry show --no-dev --tree --outdated --licenses
```

### Show dependency paths

```bash
$ poetry show --no-dev --tree --latest --path
$ poetry show --no-dev --tree --outdated --path
```

### Show dependency files

```bash
$ poetry show --no-dev --tree --latest --files
$ poetry show --no-dev --tree --outdated --files
```

<br/><br/>

## Project

### Create project

```bash
$ poetry new <project>
$ poetry new <project> --src
$ poetry new <project> --name <project>
$ poetry new <project> --src --name <project>
```

### Create project from existing source

```bash
$ poetry init
$ poetry init --name <project>
$ poetry init --src
$ poetry init --src --name <project>
```

### Activate virtual environment

```bash
$ poetry shell
```

### Deactivate virtual environment

```bash
$ exit
```

### Run script

```bash
$ poetry run <script>
```

## Virtual environment

### Create virtual environment

```bash
$ poetry env use <python>
$ poetry env use <python> --force
$ poetry env use <python> --virtualenvs-in-project
$ poetry env use <python> --virtualenvs-in-project --force
```

### Show virtual environment

```bash
$ poetry env info
```

### Show virtual environment path

```bash
$ poetry env info --path
```

### Show virtual environment executable

```bash
$ poetry env info --executable
```

### Virtual environment path

```bash
$ poetry env list
```

### Virtual environment configuration

```bash
$ poetry config virtualenvs.in-project true
$ poetry config virtualenvs.path "./.venv"
```

## Cache

### Show cache

```bash
$ poetry cache list
```

### Show cache path

```bash
$ poetry cache info
```

### Clean cache

```bash
$ poetry cache clear --all
```

## Lock

### Create lock file

```bash
$ poetry lock
```

### Create lock file with options

```bash
$ poetry lock --platform <platform>
$ poetry lock --python <python>
$ poetry lock --platform <platform> --python <python>
$ poetry lock --platform <platform> --python <python> --no-hashes
$ poetry lock --platform <platform> --python <python> --no-hashes --no-build
$ poetry lock --platform <platform> --python <python> --no-hashes --no-build --no-extras
```

## Export

### Export requirements

```bash
$ poetry export
$ poetry export --dev
$ poetry export --without-hashes
$ poetry export --dev --without-hashes
```

### Export requirements to file

```bash
$ poetry export -f requirements.txt
$ poetry export -f requirements.txt --dev
$ poetry export -f requirements.txt --without-hashes
$ poetry export -f requirements.txt --dev --without-hashes
$ poetry export -f requirements.txt > requirements.txt
```
