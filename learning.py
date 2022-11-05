'''
x, y, z = [{"name": "Sunday", "age": 30, "degree": "BSc"}, 1, "i"]

print(x, y, z)
'''

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

modifyText = " Only you can satisfy my soul! "

print(modifyText.replace("soul", "being"))
chuckString = modifyText.split(" ")
#print(chuckString)
chuckStringClearned = []
for i in chuckString:
    if i == '':
        print(" ~ emptyChar ~ ")
        continue
    if "!" in i:
        i = i.replace("!", "")
    chuckStringClearned.append(i)
print(chuckStringClearned)
#octave
txt = "\110\145\154\154\157"
print(txt.casefold())
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt.lower())

sayHi = "SAY HI"
print(sayHi.lower())
print(sayHi.casefold())
print(modifyText.center(1))
print(modifyText.strip().encode())
print(modifyText.endswith(" "))
print(modifyText.expandtabs(8))
print(modifyText.casefold().count("o"))

txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x)

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())

inp = input("Enter number: ")
getDigit = ''

if inp.isdigit():
    print("Yes!")
else:
    #print("No!")
    # remove alphabet
    for i in inp:
        if i.isdigit():
            getDigit += i
print("Extract digit: ", getDigit)

if inp.isnumeric():
    print("Yes!")
else:
    getDigit = ''
    #print("No!")
    # remove alphabet
    for i in inp:
        if i.isdigit():
            getDigit += i
print("Extract digit: ", getDigit)


joinChuck = " ".join(chuckStringClearned)
print(joinChuck)

txt = "Hello Sa!"

mytable = txt.maketrans("a", "A")

print(txt.translate(mytable))
print(mytable)
