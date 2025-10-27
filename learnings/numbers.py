''''
Python Numbers

There are three numeric types in Python:
int 
float
complex

'''

#Int
x = 1
y = 34567654324567
z = -23456

print(x)
print(y)
print(z)

#Float 
#Float, or "floating point number " is a number, positive or negative, containing one or more decimals.

x = 1.23
y = 1.0
z = -34.93

print(x)
print(y)
print(z)

# Note: 
# Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
y = 12E4
z = -85.72100

print(type(x))
print(type(y))
print(type(z))

# Complex 
# complex numbers are written with a "J" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#  Type Conversion
x = 1 #int
y = 2.8 #float
z = 3j #complex

#convert from int to float
res = 30
print(type(res))
res1 = float(res)
print(type(res1))

#convert from float to int
a = int(y)
print(a)
print(type(a))
