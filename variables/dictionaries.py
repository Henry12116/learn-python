# dictionaries also let you store a bunch of data in a single variable
from re import M


myFirstDictionary = {"name": "John", "age": 30, "city": "New York"}

# The difference between lists and dictionaries is how they are accessed
# Lists are accessed by index, dictionaries are accessed by key
# If you remember our lists...
exampleList = [1, 2, 3, 4]

# You can access the first item in the list by indexing it with 0
print(exampleList[0])

# In a dictionary, you can access the "value" by using the "key"
# The key is the name of the value you want to access
# Think of a dictionary IRL... how do you use it? You look up the definition (value) by the word (key)
# A python dictionary is no different
print(myFirstDictionary["name"])

# Again, we can check the type of myFirstDictionary
print(type(myFirstDictionary))

# Also again we can get the length of the dictionary
print(len(myFirstDictionary))

# And also again we can also see what methods we have available to us
print(dir(myFirstDictionary))

"""
['__class__', '__contains__', '__delattr__', '__delitem__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', 
'__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 
'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""
# Let's see what we can do with dictionaries
# myDict.get() will return the value of a key if it exists
# Why would we use myDict.get("key") instead of myDict["key"] if they do the same thing?
# Because if the key doesn't exist, myDict.get("key") will return None, but myDict["key"] will throw an error. Try it yourself!
print(myFirstDictionary.get("name"))

# myDict.items() will return a list of tuples containing the key and value
print(myFirstDictionary.items())

# myDict.keys() will return a list of all the keys in the dictionary
print(myFirstDictionary.keys())

# myDict.values() will return a list of all the values in the dictionary
print(myFirstDictionary.values())

# myDict.pop() will return and remove the specified key+value from the dictionary
print(myFirstDictionary.pop("name"))

# myDict.setdefault() will set a key to a default value if it doesn't already exist
print(myFirstDictionary.setdefault("favorite_food", "spaghetti"))

# myDict.update() will add a key and value to the dictionary
print(myFirstDictionary.update({"favorite_food": "pizza"}))

# You can also insert into a dictionary by doing
myFirstDictionary["favorite_food"] = "pasta"

# HOMEWORK
# Create a variable called myDatabase and set it equal to an empty dictionary
# I want you to insert three users into myDatabase (usernames: "john123", "jane456", "joe789")
# the usernames will be they keys of myDatabase, and the value will be another dictionary with the following keys: "name", "age", "city" (make up the values for these)
# After you insert the users, print out the entire dictionary
# print out the value of the "age" key for the user "joe789"
# update the "age" value for the user "jane456" by one year
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======

import pprint
myDatabase={}
myDatabase['john123'] = {'name': 'Bingo', 'Age': 84, 'City': 'Newfoundland'}
myDatabase['jane456'] = {'name': 'Bongus', 'Age': 12, 'City': 'Right Here'}
myDatabase['joe789'] = {'name': 'Bango', 'Age': 9001, 'City': 'Dinkelberg'}
pprint.pprint(myDatabase)

print(myDatabase['joe789'].get('Age'))

myDatabase['jane456'].update({'Age': 12+1})
print(myDatabase['jane456'].get('Age'))

>>>>>>> Stashed changes
=======


>>>>>>> Stashed changes
