# exceptions allow you to handle errors gracefully
# what do we mean by gracefully?

# when an error is handled gracefully, the program doesn't crash
# you may be able to continue running the program, or you may be able to exit the program in a controlled manner


# lets look at an example

# Line 11 will crash our script. You can uncomment to try, but I have left it commented so the script will run.
# print(1/0)

# You'll notice we get a ZeroDivisionError and the program crashes. This is because we are trying to divide by zero, 
# which is not allowed in math.


# What if we wanted to handle this error gracefully? We can use a try/except block to do this.

try:
    print(1/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

print("the program is still running!")

# Notice how the program continued running after the error was handled. This is because we handled the error gracefully.
# In a real program, you would want to do something more than just print a message to the user. You may want to log the error, or
# you may want to try to recover from the error and continue running the program. It all depends on what your program is doing.


# Lets look at how we can define our own exceptions

# We can define our own exceptions by creating a class that inherits from the Exception class
# We can then raise our custom exception using the raise keyword

class MyCustomException(Exception):
    pass

# On line 40 we raise our custom exception (uncomment to try)
# raise MyCustomException("This is my custom exception!")

# You'll notice that we get a stack trace when we raise our custom exception. This is because we didn't handle the exception.
# If we want to handle our custom exception, we can do so using a try/except block

try:
    raise MyCustomException("This is my custom exception!")
except MyCustomException:
    print("I caught my custom exception!")

# You'll notice that we don't get a stack trace when we handle our custom exception. This is because we handled the exception.


# Custom exceptions are useful when you want to handle a specific error in a specific way


# Homework
# Create a Person class with the following attributes: name, age
# Create a custom exception called InvalidAgeError
# When creating a person, if the age is less than 0 or greater than 120, raise an InvalidAgeError

