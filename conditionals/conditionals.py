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
if 1 + 1 == 2:
    print("1 + 1 is equal to 2")
elif 1 + 1 == 3:
    print("1 + 1 is equal to 3")
else:
    print("1 + 1 is not equal to 2 or 3")
