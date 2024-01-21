# Python Notes

1. Get all the methods and attributes of a class/object:

```python
# Assuming you have an instance of the SOME_CLASS object called SOME_CLASS
# Get the list of all attributes of the SOME_CLASS object
attributes = dir(SOME_CLASS)
# Filter out the function names
function_names = [name for name in attributes if callable(getattr(SOME_CLASS, name))]
# Print the function names
for name in function_names:
    print(name)
```

