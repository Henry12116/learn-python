# classes let you organize data and functionality into different structures
# You can think of classes as blueprints for objects

# names of classes start with a capital letter
class Hello:
    # this is called the constructor
    def __init__(self, name) -> None:
        self.name = name

    def say_hello(self):
        print("hello " + self.name)


# creating an object
h = Hello("henry")

# using methods the object has
h.say_hello()


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

# ^^^ These things come up on interviews sometimes!!! You should learn these!

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
class Person:
    is_alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is " + self.name)

    def birthday(self):
        self.age += 1

    def died(self):
        self.is_alive = False


class Student(Person):
    from random import randint

    def __init__(self, *args, **kwargs):
        super().__init__(args[0], args[1])
        self.grade = kwargs.get("grade", 1)

    def say_hello(self):
        print("Hello, my name is " + self.name + " and I'm a student")

    def make_presence_known(self):
        options = ["here", "present", "wassup", "booba"]
        random_choice = options[randint(0, len(options) - 1)]
        print(f"{self.name} says: {random_choice}")


class Teacher(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(args[0], args[1])
        self.subject = kwargs.get("subject", "math")

    def say_hello(self):
        print("Hello, my name is " + self.name + " and I'm a teacher")

    def say_start_role_call(self):
        print(f"{self.name} says: Starting role call!")


class School:
    def __init__(self, name, students, teachers):
        self.name = name
        self.students = students
        self.teachers = teachers

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def start_class(self):
        print("Class is starting!")

    def role_call(self):
        self.teachers[0].say_start_role_call()

        for student in self.students:
            student.make_presence_known()


from random import randint

students = []
teachers = []
for i in range(100):
    new_student = Student("Student " + str(i), i, grade=randint(1, 200))
    new_teacher = Teacher("Teacher " + str(i), i, grade=randint(1, 200))
    students.append(new_student)
    teachers.append(new_teacher)


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


class School:
    def __init__(self, people):
        self.people = people


# Homework
# Create a zoo class and five animal classes (you can have whatever animals you want)
# The zoo class should have a name and take a list of animals as part of its consturctor
# Each animal should have a name, a type (as in mammal or reptile), and an age as part of its constructor
# Each animal should have a the following methods:
#   1. say_hello() - prints out a greeting
#   2. eat() - prints out a statement about how it is eating
#   3. sleep() - prints out a statement about how it is sleeping
#   4. wake() - prints out a statement about how it is waking
#   5. feel free to add any other methods you want
# The zoo should have the following methods:
#   1. visit_attraction() - picks a random animal, then calls a random method that animal has showing the animals status

# When making an instance of your zoo, you should pass in at least 100 random animals


# uh oh changes
