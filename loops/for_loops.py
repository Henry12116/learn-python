# loops let you repeat a block of code
# for example:
for i in range(5):
    print(i)

# without loops, we would do shit like this:
print(1)
print(2)
print(3)
print(4)
# ...

# D.R.Y. (Don't Repeat Yourself)
john = "John"
doe = "Doe"
for i in range(100):
    print(john, doe)


for thing in [1, 2, 3, 4]:
    print(thing)


for fuck in "abcdefghijklmnopqrstuvwxyz":
    print(fuck)


# you can also do nested loops
# example:

# [0,1,2,3,4]
for i in range(5):
    # [0,1,2,3,4,5,6,7,8,9]
    for j in range(10):
        print(i, j)


# you can also use a for loop to iterate over a dictionary
# example:
my_dict = {"name": "John", "age": 30}
for key, value in my_dict.items():
    print(key, value)


# you can use for loops for list comprehensions
# let's say we wanted to create a list of 100 random numbers

# without list comprehensions:
from random import randint

random_numbers = []  # create an empty list
for i in range(100):
    random_numbers.append(randint(1, 10000))


# with list comprehensions:
random_numbers = [randint(1, 10000) for i in range(100)]

# lastly, you can use for loops for dictionary comprehensions
alphabet = "abcdefghijklmnopqrstuvwxyz"
random_number_for_each_letter = {}

# without dictionary comprehensions:
for letter in alphabet:
    random_number_for_each_letter[letter] = randint(1, 10000)

# with dictionary comprehensions:
no_cap = {letter: randint(1, 10000) for letter in alphabet}

# https://riptutorial.com/python/example/767/conditional-list-comprehensions
# you can add conditionals to your comprehensions, by putting an if statement at the end of your for loop
# for example we'll create a list of animals, each animal has a 33.3% (repeating of course) chance of being included
all_animals = [
    "cat",
    "dog",
    "bird",
    "fish",
    "snake",
    "lizard",
    "turtle",
    "hamster",
    "rabbit",
    "pig",
]
final_list_of_animals = [animal for animal in all_animals if randint(1, 11) <= 3]

# Homework
# print the numbers from 1 - 100,000
# Hardmode: only print the numbers that are multiples of 3
# Extra hardmode: only use list comprehension
