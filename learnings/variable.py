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
