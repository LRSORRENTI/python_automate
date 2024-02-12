# MYENV AND LOCAL ENVIRONMENTS

### NOTE: myenv wasn't working with pyperclip, so it suggested .venv which is a virtual environment, which is also activated with

```
source .venv/Scripts/activate
```

Not 100% sure why the below myenv/Scripts/activate stopped working

## Don't forget to run activate to enable all local python dependencies in the requirements.txt file

```
source myenv/Scripts/activate
```

## And when finished run:

```
 deactivate
```

## Introduction

This project uses a Python virtual environment to manage dependencies, ensuring that our development and production setups are consistent and isolated from the global Python installation.

## Setting Up the Virtual Environment

### Creating the Virtual Environment

To create an isolated development environment, run the following command:

```bash
python -m venv myenv
```

This command creates a myenv directory in your project, containing a local Python interpreter and directories to hold project-specific versions of Python packages.

### Activating the Virtual Environment

Before starting development, activate the virtual environment using the appropriate command for your operating system:

Windows:

```
myenv\Scripts\activate
```

Unix or MacOS:

```
source myenv/bin/activate
```

You should see (myenv) in your command prompt, indicating that the virtual environment is active.

### Deactivating the Virtual Environment

To stop using the virtual environment and revert to your global Python environment, deactivate it using:

```
deactivate
```

### Managing Dependencies

Install project-specific packages using pip while the virtual environment is active. For example, to install pyperclip, use:

```
pip install pyperclip
```

### Generating the requirements file:

To ensure consistency across environments, generate a requirements.txt file by running:

```
pip freeze > requirements.txt
```

This file can be used to install the necessary packages in another environment or by another developer using:

```
pip install -r requirements.txt
```

### Excluding the Virtual Environment from Version Control

The myenv directory should not be included in your version control system. Add it to your .gitignore file:

```
myenv/
```

### Benefits of Using a Virtual Environment

- Isolation: Each project can have its own dependencies, independent of other projects.

- No Conflicts: Avoids version conflicts between project-specific packages and global packages.

- Reproducibility: requirements.txt ensures that the same versions of packages can be installed in different environments.

- Clean Global Environment: Keeps your global Python installation clean and reserved for system-wide packages.

Using a virtual environment is a best practice in Python development. It keeps your project's dependencies isolated, your global Python environment clean, and makes your projects more portable and easier to collaborate on with others.
