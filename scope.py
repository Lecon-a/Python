# A variable's scope is a region where that variable can be access.

'''
    There are two variable's scopes
    1 - Local
    2 - Global
'''

# LOCAL Variable
def force(m):
    # a is a local variable because it can only be accessed with the force() function
    a = 9.8
    def compute(mass):
        return mass * a
    return compute(m)

f = force(10)
print(f"the weight of the object is {f}Nms^-2")    

# GLOBAL Variable
ACCELERATION = 9.80

def displayConstant():
    print(f"Acceleration due to gravity constant is {ACCELERATION}ms^-2")

displayConstant()    

# Note: global keyword can be used to change the local scope to global scope.
# And you can also use it to change the value of the global variable inside a function.