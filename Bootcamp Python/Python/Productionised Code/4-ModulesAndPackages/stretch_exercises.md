1. Create a Data Processing Package:
**Task**: Create a package named `data_processing` with a module named `cleaning`.
Within the `cleaning` module, define a function named `remove_duplicates` that takes a list as input and returns a list with duplicates removed.


2. Import and Use Module:
**Task**: Create a new Python script named `data_analysis.py` outside the `data_processing` package.
Import the `remove_duplicates` function from the `data_processing.cleaning` module.
Create a sample list with duplicates and call the `remove_duplicates` function to clean the list.
Print the cleaned list to verify correctness.

3. Extend the Package:
**Task**: Add a new module named `transforming` to the `data_processing` package.
Within the `transforming` module, define a function named `capitalise_strings` that takes a list of strings as input and returns a list with all strings capitalised.
Modify the `data_analysis.py` script to import the `capitalise_strings` function from the `data_processing.transforming` module.
Create a sample list of strings and call the `capitalise_strings` function to transform the strings.
Print the transformed list to verify correctness.

4. Conditional Execution in Modules:
**Task**: Add a conditional statement to the `cleaning.py` module that prints a message when the module is executed as a script.
Ensure that the message is only printed when the module is run directly and not when it's imported into another script.
Test the behavior by running the `cleaning.py` module as a script and importing it into the `data_analysis.py` script.

5. Use Package-Level Imports:
**Task**: Add a package-level function named `merge_lists` to the data_processing package.
Modify the `data_analysis.py` and create two additional sample lists and call the `merge_lists` function to merge them.
Print the merged list to verify correctness.