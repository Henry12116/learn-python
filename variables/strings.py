# strings are used for storing text, for example
myString = "hello world"

# if we check the type, we can see it is indeed a string
print(type(myString))

# let's look at all the functions available to us for strings
# dir() is a built in method that does exactly that
print(dir(myString))

# We see the following output
"""
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
'__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode','endswith', 
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

# we can use any of the above functions (aka methods) by doing
# "my string".function()
# ex.
print(myString.upper())

# another method we have available to us is .format()
# this method is great for formatting strings with variables
# ex.
anotherString = "world"

# you dont have to call this var, you can also name this whatever you want
print("hello {var}".format(var=anotherString))




