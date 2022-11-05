def globalVal():
    # with global keyword we can create a global variable inside a function
    global x
    x = 4
    y = x * x
    return y

functionResult = globalVal()

#print("Function returns:: ", functionResult, " Get the global variable value::", x)
byn = b'01101'

x = range(6)

#display x:
print([i for i in x])
print(x)

#display the data type of x:
print(type(x))
#to check the loc a variable in memory
x = memoryview(bytes(4))

#display x:
print(x)

#display the data type of x:
print(type(x))

x = 1e-3j
y = 3565622255488771186758476950859478473654079568758759657846497578060788759647575858
z = -3255522

print(complex(z))
print(y)
print(type(z))

import random

print(random.randrange(1, 10))

para = """
I am so glad that Jesus loves me,
Jesus loves me. Jesus loves me.
"""

print("Multiline string ::> ", para)

isCharPresent = bool("Jesus" in para)
print("Is Jesus present in paragraph? ", isCharPresent)
