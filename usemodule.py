# User defined module
import module as m
# Built-in module
import platform

x = platform.system()
print(x)

m.greeting("Sunday")
print(m.person1["name"])

'''
    Using the dir() Function
    There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
'''
print(dir(x))
print(dir(m))

'''
    Import From Module
    You can choose to import only parts from a module, by using the from keyword.
'''
