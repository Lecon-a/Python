import datetime

x = datetime.datetime.now()

print(x)
print(x.year)
print(x.strftime("%U"))
print(x.strftime("%c"))
print(x.utcnow())
# print(dir(datetime.datetime.now()))

# To create a date, we can use the datetime() class (constructor) of the datetime module. (w3schools)
x = datetime.datetime(2020, 5, 17)

print(x)
