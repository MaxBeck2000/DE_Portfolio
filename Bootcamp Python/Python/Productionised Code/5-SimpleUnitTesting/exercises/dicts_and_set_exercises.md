# Dicts and Sets Exercises

Create a file `dict_sets.py` and in this file define a function for each of the questions below:  
## Exercise 1

Write a function called `cleanup_address_book`, that accepts a single argument: an 'address book' dictionary in which the keys are the names and the values are the numbers (stored as strings). The function should return a new dictionary, holding the names and numbers as the original, except that: all names should be in title case, separated by a single space if there is more than one name; all numbers should be stored as strings (not integers), with a single space before the last six digits (if there are eight or more digits in the number).

## Exercise 2

Write a function called `search_address_book`, that accepts two arguments: an 'address book' dictionary in which the keys are the names and the values are the numbers (stored as strings), and a search string. The function should return a dictionary that contains all the entries in the original address book, for which the name starts with the search string.

## Exercise 3

Write a function `count_vowels` that accepts a string and return a dictionary that contains each of the five vowels as keys. The corresponding values should represent that number of occurrence of each vowel, in the input string. For example, the input string  'hello world' will return the dictionary:
`{'a':0, 'e':1, 'i':0, 'o':2, 'u':0} `

## Exercise 4

Write a function called `get_names_in_common`, that accepts a two arguments: each being an 'address book' dictionary in which the keys are the names and the values are the numbers (stored as strings). The function should return a set of names. This set contains all the names that appear in both address books.

## Exercise 5

Write a function called `get_numbers_in_common`, that accepts a two arguments: each being an 'address book' dictionary in which the keys are the names and the values are the phone numbers (stored as strings). The function should return a  set of (string) phone numbers. This set contains all the numbers that appear in both address books.

## Exercise 6

Write a function called `combine_address_books`, that accepts two arguments: each being an 'address book' dictionary in which the keys are the names and the values are the phone numbers (stored as strings). The function should return a  tuple of two dictionaries (that also contain name and number strings). The first returned element contains all the elements in the first input address book, additionally with all names in the second address book that aren't already in the first address book. The second element of the returned tuple is also a dictionary: it contains those elements of the second address book that weren't able to be added to the first returned element.
