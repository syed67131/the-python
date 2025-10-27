# Strings in the python are surrounded by either single qutation marks, or double quotation marks.

# 'hello' is same as "hello"

print('hello')
print("hello")

# QUOTES inside Quotes:
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He's called 'Johnny")
print('He is called "Johnny')


# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

a = '''  
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.

'''

a = "Hello World!"
print(a[1])

# Looping Through a String
# since strings are arrays, we can loop through the characters in a string, with while loop.
# Loop through the letters in the word banana
for x in "banana":
    print(x)

print("start")
for x in "banana":
    print(x)
    print("end")

# String length
# to get the length of a string, use the len() function.
# Note : when we count length it start from 1 and also include empty space
a = "hello world"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best thing in life are free!"
if "free" in txt:
    print("Yes, 'free' is present")

    # Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("true it is not")
# print("expensive" not in txt)

b = "Hello, world"
print(b[2:5])

# Slice From the start
# by leaving out the start index, the range will be start from the first character.

# Get the characters from the start to position 5 (not included)
b = "Hello world"
print(b[:5])

cd = "compactDisk"
print(cd[:7])


# Slice To the End
# By leaving out the end index, the range will go to the end:
# Get the characters from position 2, and all the way to the end:

da = "Hello world!"
print(da[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
c = "Hello, world"
# print(b[-5:-2])
print(c.strip())
print(c.replace("b", "d"))

