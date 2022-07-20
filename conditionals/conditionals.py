# conditionals lets you check if a condition is true or false
# if the condition is true, then the code inside the if statement will be executed
# if the condition is false, then the code inside the else statement will be executed
# for example:

if 1 + 1 == 2:
    print("1 + 1 is equal to 2")
else:
    print("1 + 1 is not equal to 2")


# any expression can be used in the if statement, as long as it evaluates to a boolean
# for example:
if True:
    print("this will always execute")
else:
    print("this will never execute")

# or
if False:
    print("this will never execute")
else:
    print("this will always execute")


# you can also use not to invert a boolean
# for example:
if not True:
    print("this will always execute")
else:
    print("this will never execute")


# certain types have a built-in boolean representation
# meaning they have a "truthy" or "falsy" value
# for example:
print(bool(0))
print(bool(1))

# strings have a truthy value
print(bool(""))

# None has a falsy value
print(bool(None))

# this can be useful when you want to check if a variable has a value, execute a code block, or do nothing
# for example:
thing = None
if thing:
    print(thing.upper())
else:
    print("thing is None")


# or
thing = "hello"
if thing:
    print(thing.upper())
else:
    print("thing is None")


# lastly you can use elseif to check for multiple conditions
# conditionals are evaluated from top to bottom
# for example:
user_logged_in = True
condition = user_logged_in

if condition:
    print("Entered if block")
elif True:
    print("Entered elif block")
else:
    print("1 + 1 is not equal to 2 or 3")


thing = {"name": "John", "age": 30}
if thing["name"] == "John":
    if thing["age"] < 13:
        print("John is a child")

    elif thing["age"] < 18:
        print("John is a teenager")
    else:
        print("John is an adult")
else:
    print("This is not John, and we don't care")


# Homework
# set a variable equal to a random number between 1 and 100
# at the top of your homework, write "from random import randint" (no quotes)
# set a variable equal to my_random_number = randint(1, 100)
# using conditionals, print "the number is even" if my_random_number is even
# or print "the number is odd" if my_random_number is odd (raging clue in variables/numbers.py)

#HW
from random import randint
x=randint(1,100)
if x%2==0:
    print("x is even")
else:
    print("x is not even")