setA = {8, 1, 2, 7, 4, 5, 3, 6}

# for i in range(len(setA)):
#     print(setA)

fruit1 = {"orange", "mango", "apple", "papaya"}
fruit2 = {"pineapple", "tomatoes", "cucumber", "grape"}

fruit1.update(fruit2)
print(fruit1)

fruit1.remove("mango")
fruit1.discard("cucumber")

removeUndeterminedItem = fruit1.pop()
print(removeUndeterminedItem)
print(fruit1)
fruit1.clear()
print(fruit1)
#delete the entire set and its items
del fruit1
#check for the deletion
#print(fruit1)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = y.issubset(x)
a = x.issubset(y)

print(z, " ", a)
