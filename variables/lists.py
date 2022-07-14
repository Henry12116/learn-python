# lists let you store a bunch of data in a single variable
myFirstList = [1, 2, 3, 4, 5]

# they can contain whatever you want, you could even have a mix of different data types in the same list
# ex.
mySecondList = [1, "a", 2, "b", 3, "c"]

# again we can check the type of myList
print(type(myFirstList))

# we can get the length of the list
print(len(mySecondList))

# and we can also see what methods we have available to us
print(dir(mySecondList))

"""
['__add__', '__class__', '__class_getitem__', '__contains__',
'__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
'__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
'__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
'__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

# look at all those methods :-)
# let's see what we can do

# list.count() will count the number of times a value appears in the list
print(mySecondList.count("a"))

# list.index() will return the index of the first instance of a value in the list
print(mySecondList.index("a"))

# list.append() will add a value to the end of the list
print(mySecondList.append("d"))

# list.remove() will remove the first instance of a value in the list
print(mySecondList.remove("a"))

# list.reverse() will reverse the order of the list
print(mySecondList.reverse())

# list.sort() will sort the list in alphabetical order
# in order for sort to work, the types must be the same
print(myFirstList.sort())

# list.clear() will remove all values from the list
print(mySecondList.clear())

# list.copy() will return a copy of the list
print(mySecondList.copy())

# list.pop() will remove the last item in the list
print(mySecondList.pop())

# list.insert() will insert a value at a specific index
print(mySecondList.insert(1, "b"))

# list.extend() will add a list to the end of the current list
print(mySecondList.extend(["e", "f"]))

# similar to strings, we can use the + operator to combine lists
print(myFirstList + mySecondList)

# we can also index lists like strings
# this will print the value at index 0
print(mySecondList[0])

# lets grab the last element of the list
print(mySecondList[-1])


# HOMEWORK
# create a list of your favorite animals
# print the length of the list
# print the last element of the list
# print the first element of the list
# print the 3rd element of the list
# print the list in reverse order
# print the list in alphabetical order
