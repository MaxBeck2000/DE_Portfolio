# Clean Code

Clean code means writing code that is easy to read, understand and maintain.
It is a set of coding practices and principles that promote clear, simple and readable code.
Writing clean code is essential for developer collaboration and the long-term maintainability of software.

**Refactoring** involves restructuring code to producer cleaner code, while preserving its original functionality.

## Principles of Clean Code

### 1. Readability

Writing code that is easy for others to understand.

- Use meaningful variable and function names
- Comments and Documentation:
  - Use comments sparingly and focus on writing self-explanatory code e.g. avoid a complex solution to a problem in favour of one that can be clearly understood.
  - When comments are necessary, use them to explain the 'why' of a code snippet and not the 'how'.
  - Provide documentation to explain the purpose of the codebase as a whole and the overall architecture.
- Use whitespace to separate logical blocks of code.

> The Zen of Python:\
> `Beautiful is better than ugly.`\
> `Explicit is better than implicit.`\
> `Readability counts.`\
> `Sparse is better than dense.`

### 2. Simplicity

Avoid unnecessary complexity and strive for the simplest solution that meets the requirements.

> The Zen of Python:\
> `Simple is better than complex.`\
> `Complex is better than complicated.`

### 3. Consistency

Follow a consistent style guide and naming conventions throughout a project. [PEP 8](https://peps.python.org/pep-0008/) is the most widely recognised and officially endorsed style guide for Python code. Some of the conventions discussed in Pep 8 include:
- Including two empty lines before each function definition
- Including a space either side of operators, e.g. '`x == y`' not '`x==y`'
- Removing all unused imports
- Removing variables that have been assigned but never used
- Using lower-case names for objects and functions
- Using title-case names for classes 


> The Zen of Python:\
> `Special cases aren't special enough to break the rules.`\
> `Although practicality beats purity.`

### 4. Avoid Code Duplication: DRY (Don't Repeat Yourself)

- Create reusable variables, functions or modules. This reduces chances of bugs and makes maintenance easier.
- A rule of thumb is if you find yourself repeat a snippet of code more than twice, consider making it a function/variable.

### 5. Modularity and the Single Responsibility Principle (SRP)

- Divide code into small sections that perform a specific task.
- Uphold the SRP by ensuring each section possesses a clear, singular responsibility, and be easy to understand independent of other code.

