# Linting


## What is Linting?
Linting is the process of analysing code for potential errors, bugs, or stylistic inconsistencies. Linters, or lint tools, examine source code and flag any issues that deviate from a predefined set of rules or coding standards. Once there are no isses in the code, the code is considered **'lint-free'**.

## Why is Linting Important?
Linting offers several benefits to developers and teams working on Python projects:

- **Catching Errors Early**: Linters can detect syntax errors, typos, and common programming mistakes before the code is executed, helping developers catch and fix issues early in the development process.

- **Enforcing Coding Standards**: Linting tools enforce coding conventions and style guidelines, ensuring consistency across the codebase. 

- **Enhancing Readability**: Linters can flag code that is difficult to read or understand.

## Implementing Linting in Python Projects
There are several linting tools available for Python, each with its own set of features and capabilities, we will look at **Pylint**. 

Pylint is a widely used Python static code analyser that checks for errors, enforces coding standards, and offers code quality insights. It incorporate many checks based off [PEP 8](https://peps.python.org/pep-0008/), the official Python style guide, and can be run directly on Python files or integrated into popular code editors and IDEs, such as Visual Studio Code or PyCharm. 

### Running Pylint Directly
When running directly on a Python file or directory, Pylint will analyse the code and display a number of messages indicating potential issues or violations of coding standards, as well as some statistics about the number of warnings and errors found in different files. To use Pylint this way:
1. **Installation**:  If you haven't already installed Pylint, you can do so using pip, the Python package manager:
```
pip install pylint
```
2. **View Linting Results**: Once installed, you can run Pylint on your Python files or entire projects. From the command line, navigate to your project directory and run:
```
pylint your_file.py
```
Replace `your_file.py` with the name of your Python file or directory you want to lint.

This is using a relative path, alternatively, you can use an absolute path to lint files located outside of the current directory:
```
pylint /path/to/your_file.py
```
Replace `/path/to/your_file.py` with the absolute path to your Python file or directory you want to lint. 

### Integrating Pylint with VS Code
VS Code has built-in support for Pylint, allowing you to easily integrate it into your development workflow. To use Pylint this way:

1. **Installation**: Install the Pylint extension for VS Code. You can find it in the Extensions view by searching for "Pylint" and clicking on Install.

2. **View Linting Results**: Open a Python file in VS Code, and you should see linting suggestions and errors highlighted in the editor. VS Code displays Pylint messages in the Problems panel and as squiggly lines in the editor.



## Formatters
Once Pylint highlights potential issues in your code, the responsibility falls on the developer to address these concerns. There are however tools which you can use to automatically change the format of your code to help in the process of making it 'lint-free'. A popular tool for this purpose is called **Black**.
Black is a PEP 8 compliant opinionated formatter and reformats entire files in place.  

### Running Black Directly
When running directly on a Python file or directory, Black will automatically reformat the code to adhere to its predefined style guidelines. To use Black this way:
1. **Installation**:  If you haven't already installed Black, you can do so using pip, the Python package manager:
```
pip install black
```
2. **Reformat with Black**: Once installed, you can run Black on your Python files or entire projects. From the command line, navigate to your project directory and run:
```
black your_file.py
```
Replace `your_file.py` with the name of your Python file or directory you want to reformat.

This is using a relative path, alternatively, you can use an absolute path to reformay files located outside of the current directory:
```
black /path/to/your_file.py
```
Replace `/path/to/your_file.py` with the absolute path to your Python file or directory you want to reformat. 

### Integrating Black with VS Code
1. **Installation**: Install the Black extension for VS Code. You can find it in the Extensions view by searching for "Black" and clicking on Install.

2. **Reformat with Black**: Once installed, you can trigger Black to format the code by using the built-in formatting shortcut (Shift+Alt+F on Windows/Linux or Shift+Option+F on macOS) or by right-clicking in the editor and selecting "Format Document". Black will automatically reformat the code according to its style guidelines, ensuring consistency and readability.
Alternatively, you can enable the "Format on Save" feature in VS Code to automatically format your code with Black every time you save a file. To enable this feature, go to VS Code settings (Ctrl+,), search for "Format On Save", and check the box. With this option enabled, your code will be formatted with Black every time you save a file, ensuring that your codebase stays consistent and maintainable.