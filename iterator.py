'''
    According to w3schools, an iterator is an object that contains a countable number of values.

    An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

    Technically, in Python, an iterator is an object which implements the iterator protocol, 
    which consist of the methods __iter__() and __next__().

    Iterator vs Iterable
    Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

    All these objects have a iter() method which is used to get an iterator:
'''

mytuple = ("apple", "banana", "cherry")
myiter = iter(mytuple)

# print(next(myiter))
# print(next(myiter))

# Note: string is an iterable object, from where iterator can be generated
name = "Sunday"
myNameIter = iter(name)

print(next(myNameIter))

'''
    w3schools' Example
    Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
'''

class AppendChar():
    def __iter__(self):
        self.a = "a"
        return self

    def __next__(self):
        if len(self.a) > 20:
            raise StopIteration
        x = self.a
        self.a += "a"
        return x

myClass = AppendChar()
myiter = iter(myClass)

for char in myiter:
    print(char)