# Modules and Packages

Modules and packages are two essential components that facilitate modularity, one of the foundational principles of clean code. Modularity involves breaking down code into smaller, self-contained units of functionality, each responsible for performing a specific task. This has several benefits:
- Logic in modules and packages can be reused elsewhere.
- Modules and packages allow for better code design and separation of responsibilities.

Simply put, **modules** are Python files, containing code, such as functions and variables, encapsulating specific functionalities or data. On the other hand, **packages** are collections of related modules (and sub-packages) organised hierarchically within directories. 

## Modules:
Modules are primarily made to be used in other modules or other parts of a Python program. To "use" a module means to access and utilise the objects defined within that module in your Python code. 

To do this, we have to import the module into our code. 

### Importing Modules
Suppose we have a module `example_module` which has the following contents:
```Python
# example_module.py
def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2"


print("Hello world!")

``` 
There are a few different ways of importing this module into into our program:

1. **Using `import`**  

Importing a module using the `import <module_name>` syntax means that any functions, classes, variables, or other objects defined within that module become available for use in your code. To access these objects, you use the dot notation, combining the module name with the specific object name you want to use.  

**Note**: The name of a module is derived from the file name without the `.py` extension. 

In the above case, after importing `example_module`, we can access the functions `add` and `subtract` as follows:
```Python
# my_script.py
import example_module

add_result = example_module.add(1, 2)
subtract_result = example_module.subtract(1, 2)

```
It's important to note that after executing `my_script.py`, you will see `'Hello world!'` printed out, despite no explicit `print('Hello world')` in this file. This is because when a module is imported, Python runs all the code in that module, before loading all objects defined in that module into the namespace of our code (through the name of the imported module). So in the line `import example_module`, the entirity of the code in `example_module` is executed, including the `print('Hello world!')`. Only after that are `add` and `subtract` then made accessible within `my_script.py` using the dot notation. 

2. **Using `from` and `import`**

Alternatively, you can import specific objects from a module directly into the current namespace using the `from <module_name> import <symbol>` syntax. This approach allows you to access the imported objects without needing to prefix them with the module name. It does mean that only the object specified from the module is made accessible.

For example, we can import the `add` function directly from the `example_module` module. What this means is we can now access the `add` function as follows:

```Python
# my_script.py
from example_module import add

add_result = add(1, 2)

```
Since we only have imported the `add` function, we do not have access to the `subtract` function. 

After executing `my_script.py`, you will see `'Hello world!'` printed out. Whilst only one object from the module has been imported, Python still has to execute the whole module before loading that object directly into the namespace of our code. 

3. **Using `as`**

The `as` keyword in Python allows you to alias imported modules or objects with a different name. 

For example, we can import `example_module` but alias it as `ex_m`. What this then means is we can use the alias `ex_m` to access objects from `example_module`: 

```Python
# my_script.py
import example_module as ex_m

add_result = em.add(1, 2)

```
Similarly, you can use `as` with the `from ... import ...` syntax to alias imported objects:
```Python
# my_script.py
from example_module import add as ex_m_add

add_result = ex_m_add(1, 2)

```

### Executing Modules as a Script
Since modules are just Python files, they can be executed just like any other Python script, (i.e running `python module_name.py` from the command line). 

So a module can be imported elsewhere in a program as well as being run directly. Because of this versatility, a very common construct used in Python files is the conditional expression `if __name__ == '__main__'`. 
In short, this construct allows you to execute code when the file runs as a script, but not when it is run as a module.

#### How `if __name__ == '__main__'` works:

- When you run a Python script directly (e.g., `python example_module.py`), Python assigns the special variable `__name__` to `'__main__'`, indicating that this script is the main program being executed.
- When you import a Python script as a module into another script (e.g., `import example_module`), Python assigns `__name__` to the name of the module (`'example_module'` in this case), indicating that it is being imported.
- Therefore, by using this construct, you can include code that should only be executed when the script is run directly, and not when it's imported as a module. This avoids running code that’s irrelevant for imported modules.

For instance, suppose the code in `example_module` was updated with the following content:
```Python
# example_module.py
def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return f"num_1 - num_2 is: {num_1 - num_2}"


print(f"__name__ is currently: {__name__}")

if __name__ == "__main__":
    print("This code is only executed when the module is run as a script.")

```
In this example, the `print(f"__name__ is currently: {__name__}")` statement will always execute regardless of how the module is used. However, the code block under `if __name__ == '__main__':` will only execute if the module is run directly as a script, since this is the scenario when `__name__` is set to `"__main__"`. When the module is imported, `__name__` will be set to `'example_module'`, meaning the code block will not execute. 

## Packages:

Packages allow a collection of modules and subpackages (packages within a package) to be grouped together under a common package name. 

Essentially a package is a directory containing Python modules and subpackages. These directories contain a special file named `__init__.py`, (unless using a [namespace package](https://docs.python.org/3/glossary.html#term-namespace-package), which is beyond the scope of this course), which will be executed upon importing the package or any of its modules / subpackages. While the `__init__.py` file is often left empty, since it is executed on importation, it can contain initialisation code such as importing modules or subpackages within the package, defining package-level objects or setting up configurations.



### Importing with Packages

#### **Importing a Module within a Package**
The syntax for importing modules from a package closely resembles that of importing a standalone module. The key distinction lies in specifying the module's path, which utilises dot notation. This notation combines the package name, any subpackages, if applicable, and finally the module name itself, all separated by dots.

Suppose we are working with a package of the following structure:
```
mypackage/
├── __init__.py
├── mymodule1.py
├── mymodule2.py
└── subpackage/
    ├── __init__.py
    └── submodule.py
```

1. **Using `import`**

This imports an entire module into our code. 
```Python
# my_code.py
import mypackage.mymodule1
mypackage.mymodule1.mod1_function()
```
In this case, we import the entire `mymodule1` into our code, and then we can access its functions using dot notation.

2. **Using `from` and `import`**

Depending on its useage, this will either import an entire module into our code or a specific object defined within a module. 
```Python
# my_code.py
from mypackage import mymodule2
mymodule2.mod2_function()
```
Here, we are importing the entire `mymodule2` into our code, so we have access to all objects defined within through the dot notation.
```Python
# my_code.py
from mypackage.mymodule2 import mod2_function
mod2_function()
```
Here, we import only the function `mod2_function` into our code. 

3. **Using `as`**

```Python
# my_code.py
from mypackage.subpackage import submodule as sm
sm.submod_function()
```

In all of these cases, the `__init__.py` file of `mypackage` is executed upon importation. Similarly, when importing from within subpackage, the `__init__.py` file of subpackage is also executed.

#### **Importing a Package / Subpackage**
Above we have imported a modules and objects from within a package. It is possible to import a package into your code as well. 

For example, you can do the following:
```Python
# my_code.py
import mypackage
```
What's important to note is that this action does not inherently grant access to the packages modules, subpackages, or submodules within the package. What it does is create an empty namespace `mypackackage` as well as execute the package's `__init__.py` file. Therefore, if you want to ensure that some of the contents of the package are accessible upon import, it's essential to define what gets imported in the `__init__.py` file of the package. 

For example, to ensure that `mymodule1` is always accessible when `mypackage` is imported you can include this in the `__init__.py` file of `mypackage`:
```Python
# mypackage/__init__.py
from mypackage import mymodule1
```
This is known as making `module1` a package-level module. Anything you import or define in this `__init__.py` would have the package-level title, since it will be accessible directly from the package namespace.

An example of importing in the `__init__.py` file can be found in the `requests` package. The typical use case of importing this package is to do as follows:
> import requests
What this does is import the requests package into our code, which will execute the `__init__.py`. This file in turn imports further modules and subpackages from within the `requests` package. This allows us to use the `get` function defined within that package. 

## External Modules and Packages
Above we have only been looking at importing our own modules and packages which live in the same directory as the script we are executing. 
However, we can also import modules and packages which either came as part of Python's standard library (i.e `os`) as well as third party modules and packages (i.e `pandas`). So, when our Python interpreter encounters an `import` statement, it actually searches for the specified module or package across a set of directories, in the following order:

1. The directory from which the script containing the import is run. 
    - Python initially looks for the module or package in the directory from which the script containing the import statement is executed. If the script is not executed from a file, such as when running Python interactively, Python considers the current working directory as the starting point for the search.
2. The directories listed in the `PYTHONPATH` environment variable. 
    - The `PYTHONPATH` environment variable contains a list of directories that Python should include in its search path when looking for modules.
    - Python traverses through each directory listed in `PYTHONPATH`, in the order they are specified, searching for the desired module.
3. Installation-dependent list of directories:
    - During the installation of Python, an installation-dependent list of directories is configured as part of the Python environment setup. 

After gathering directories from these sources, Python combines them to form the complete search path, which is represented by the `sys.path` variable. This variable is accessible from within Python scripts and modules via the `sys` module. `sys.path` provides visibility into the directories being searched for modules, allowing developers to diagnose import-related issues and customise the module search path if necessary.

### Import Order
When writing imports statements, PEP8 recommends the following: 

- Imports should be at the top of the file, after any module comments and docstrings.
- They should be divided in to the following groups in this order:
    1. **Standard Library Imports**: Begin by importing modules from the Python standard library. These are modules that come bundled with Python and do not require external installation.

    2. **Third-Party Library Imports**: Next, import modules from third-party libraries or packages installed via tools like pip. 

    3. **Local Imports**: Finally, import modules from your own project or other local directories. These are modules that you have written yourself or are part of your project's structure.
- Each group of imports should be separated by a blank line.
- Within each group order your imports alphabetically. 