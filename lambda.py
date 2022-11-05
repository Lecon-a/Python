numbers = [1, 2, 3, 4, 5]

def pow(n):
    return lambda x : x**n

numberToIndex2 = pow(2)
numberToIndex3 = pow(3)
numberToIndex4 = pow(4)

print(numberToIndex2(2))
print(numberToIndex3(2))
print(numberToIndex4(2))

# Use lambda functions when an anonymous function is required for a short period of time.
raiseToTwo = pow(2)
x = lambda v : [raiseToTwo(x) for x in v]

print(x([1, 2, 3, 4]))
