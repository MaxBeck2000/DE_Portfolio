# Summary

- Python objects have a type, an ID and a value.
- Examples of object types include integers (`int`), floating point numbers (`float`) , strings (`str`) and lists (`list`).
- When we use the assignment operator (`=`), this can change a variable's reference to a new object, which will change the ID of the variable (to this new object's ID).
- In the above list of object types, the list is the odd one out, because we can change the value of the object (using its `append` method) without changing its ID. We say that this type is *mutable* (i.e. changeable).

For instance:

```python
x = 10
print(id(x))
x = x + 1
print(id(x))
```
`x` will now have a different id, whereas now:

```python
my_list = [1,2,3]
print(id(my_list))
my_list.append(4)
print(id(my_list))
```

`my_list` will have the same id.