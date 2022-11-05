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
