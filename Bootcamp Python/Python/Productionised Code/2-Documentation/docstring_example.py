""" A Python script that creates one function and then prints its docstring."""

def modified_add(arg1: int,arg2: int) -> str:
    """A function to add together the two arguments in a formatted string

    Args:
        arg1 (int): First integer to add
        arg2 (int): Second integer to add

    Returns:
        str: A formatted string showing the arguments and their addition
    """

    formatted_string = f'{arg1} + {arg2} - {arg1 + arg2}'
    return formatted_string

print(help(modified_add))
