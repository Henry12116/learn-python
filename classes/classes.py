# classes let you organize data into different structures
# You can think of classes as blueprints for objects

# Say this out loud 10x
# an object is an instance of a class
# an object is an instance of a class
# an object is an instance of a class
# an object is an instance of a class
# an object is an instance of a class
# an object is an instance of a class
# an object is an instance of a class
# an object is an instance of a class
# an object is an instance of a class
# an object is an instance of a class

# Python is an object oriented language, meaning that it has classes
# There are four pillars of object oriented programming:
# 1. Inheritance
# 2. Encapsulation
# 3. Polymorphism
# 4. Abstraction

# Some of these are more present than others in Python, but in other languages like Java or C++, all 4 are strongly present

# Inheritance:
# A class can inherit from another class
# This means that the child class will have all the properties and methods of the parent class
# The child class can override the parent class's methods
# The child class can also add new methods to the parent class
# For example:
class Animal:
    # this method is called the constructor
    def __init__(self, name):
        self.name = name

    def fart(self):
        print("Fart!")

    def sleep(self):
        print("I'm sleeping!")

    def speak(self):
        print("I'm an animal!")

    def eat(self):
        print("I'm eating!")

    def __str__(self):
        return self.name


class Dog(Animal):
    def speak(self):
        print("Woof!")

    def __str__(self):
        return self.name + ": Dog"


class Cat(Animal):
    def speak(self):
        print("Meow!")

    def __str__(self):
        return self.name + ": Cat"

    def __int__(self):
        return 420


# Encapsulation:
# The idea of encapsulation is to hide the implementation details of a class from the user
# In python encapsulation is rather weak
# there is not a lot you can do to hide the implementation details of a class


# Polymorphism:
# Polymorphism is the ability of an object to take on many forms
# You can use this to check if a child class is an instance of a parent class
# For example:
d = Dog("Fido")
c = Cat("Mittens")

# these will all be true
print(isinstance(d, Animal))
print(isinstance(c, Animal))
print(isinstance(d, Dog))
print(isinstance(c, Cat))

# these will be false
print(isinstance(d, Cat))
print(isinstance(c, Dog))


# Abstraction:
# abstraction is the process of identifying the essential features
# and hoisting methods/attributes to a parent class where applicable


# To create a class you could do this:
class Hello:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name)

    def __str__(self):
        return self.name


# to create an instance (aka an object) of a class you could do this:
h = Hello("Henry")

# to use methods of the class you could do this:
h.say_hello()


# EVERYTHING IN PYTHON IS AN OBJECT


# <class 'str'>
x = "test"
# x is an instance of a string class
type(x)


# <class 'int'>
y = 1
# y is an instance of an integer class
type(y)


# etc
