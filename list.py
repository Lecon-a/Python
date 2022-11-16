fruit = ["apple", "banana", "cherry"]

#list method
#append() add new item to the end of a given list
fruit.append("orange")
fruit.append("cucumber")
fruit.append("corn grain")
fruit.append("apricots")
fruit.append("grapes")
fruit.append("tomatoes")
#display
print(fruit)
#clear all element in the list
'''
fruit.clear()
print(fruit)
'''
#copy() - this returns a copy of a list
fruit_2 = fruit.copy()
print(fruit_2)
#count() - this counts and returns the total number of times a specified item occur in a given list
banana_freq = fruit_2.count("banana")
output = "Banana occurs {} {}."
freq = "time" if banana_freq <= 1 else "times"
print(output.format(banana_freq, freq))

#extend() - this add items of an iterable collection to the end of a current list
car = ["toyota", "bmw", "ford", "volvo"]
fruit.extend(car)
print("Extend fruit list with car list: ", fruit)
#index() - this returns the position of a specified item
print("What is the position of \"BMW\"?", fruit.index("bmw"))
#insert(index, item) - this method add an item to a specific position in a given list
fruit.insert(4, "lemon")
fruit.insert(9, "goron tula")
fruit.insert(5, "bitter gourd")
#display
print(fruit)
#pop - remove a specified item from a given list using its index
fruit.pop(0)
print(fruit)
#remove() - remove specified item from a given list
removedItem = fruit[fruit.index("toyota")]
fruit.remove("toyota")
output = "{} was removed from the fruit extends car list: {}."
print(output.format(removedItem, fruit))
#reverse() - this method reverses the order of a given list
fruit.reverse()
print(fruit)
#sort() - sorts list by default in ascending order
fruit.sort()
print(fruit)
#this sort() can be modified to return in a specific order
fruit.sort(reverse=True)
print(fruit)
#define function
def myFunc(item):
    return len(item)
#also a function can be passed into it.
fruit.sort(reverse=False, key=myFunc)
print("Sorted with function parameter: ", fruit)
#using list() constructor to create a new list object
thislist = list(("apple", "banana", "cherry"))
print(thislist)

print("\n:: Summary ::")
output = '''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

Note:
When choosing a collection type, it is useful to understand the properties of that type.
Choosing the right type for a particular data set could mean retention of meaning, and,
it could mean an increase in efficiency or security.
'''
print(output)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# List comprehension - shortens looping through list syntax/code
fruitsComprehension = [x for x in fruits if 'a' in x]
print("List comprehension: ", fruitsComprehension)

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
numbers = [1, 2, 3, 4, 5]
#useLambda = lambda numbers : x*2
"""
Copy a List

You cannot copy a list simply by typing list2 = list1,
because: list2 will only be a reference to list1, and changes made in list1 will automatically
also be made in list2.

There are ways to make a copy, one way \is to use the built-in List method copy().
"""
copyList = numbers
print("Copied list:", copyList)

copyList[1:3] = [23, 45, 100]
print("The changes affected the original list:", numbers)

tupleVar = ('tuple1', 'tuple2', 'tuple3')
print(tupleVar)
#unpacking tuple values into variables
t1, t2, t3 = tupleVar
print(t1, t2, t3)
#using asterisk*
t1, *t2 = tupleVar
print(t1, t2)
