x = 5
x = "five"
print(x)
x = float()
print(type(x))

##Python Variables - Assign Multiple Values

#Many values to multiple variables
x,y,z = "Orange", "Banan", "Cherry"
print(x); print(y); print(z)

##One Value to Multiple Variables
x = y = z = "Greeen"
print(x)
print(y)
print(z)

##Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


res = "the python is awesome"
print(res)

x = "python "
y = "is "
z = "easy"
print(x + y + z)

##Global Variables
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)


##The global Keyword
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

#To create a global variable inside a function, you can use the global keyword.
x = "awesome"
def myFunc():
    global x
    x = "fanastaic"

    
myFunc()

print("Python is " + x)



