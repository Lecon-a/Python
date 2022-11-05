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