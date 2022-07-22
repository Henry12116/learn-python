# functions allows us to bundle functionality
# we can then use this functionality, to do a bunch of different things

# you define functions with the def keyword
# for example:
def add(a, b):
    return a + b


x = add(1, 1)

# you can also define functions with no arguments
# for example:
def say_hello():
    print("hello")


# you can also define functions with default arguments (aka key word arguments)
# for example:
def subtract(a, b=1):
    return a - b


def greeting(name=None):
    if not name:
        print("No one to greet.")
        return

    print(f"hello {name}")
