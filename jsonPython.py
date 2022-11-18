'''
    JSON is a syntax for storing and exchanging data.

    JSON is text, written with JavaScript object notation.
'''
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x
y = json.loads(x)

# the result is a Python dictionary:
print(y)

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x, indent=4, sort_keys=True))
