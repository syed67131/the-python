# Built-in Data Types
'''
In programming, data type is an important concept.
Bariables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories.

Test Type:  str

Numeric Types: int, float, complex

Sequence Types: list, tuple, range

Mapping Type:  dict

Set Types: set, frozenset

Boolean Type: bool

Binary Types: bytes, bytearry, memoryviem

None Type: NoneType


'''


x = 5
print(type(x))

# Setting The Data Type
x = "Hello World"     #str
x = 30                #int
x = 20.5              #float
x = 1j                #complex
x = ["apple", "banana", "cherry"]       #list
x = ("apple", "banana", "grapes")       #tuple
x = range(5)                            #range
x = {"name": "john", "age": 39}         #dic
x = frozenset({"apple", "banana", "cherry"})  #frozenset
x = True        # bool
x = b"Hello"    #bytes
x = bytearray(5)             #bytearray       
x = memoryview(bytes(5))    #memoryview
x = None          #NoneType
