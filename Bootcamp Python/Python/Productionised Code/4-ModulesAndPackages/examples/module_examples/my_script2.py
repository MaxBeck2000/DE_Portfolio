"""A script to test out importing a module"""

# from example_module as ex_m

# print(ex_m.add(1,2))

from example_module import add as ex_add

print(ex_add(1, 2))
