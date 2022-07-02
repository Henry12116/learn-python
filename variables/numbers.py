# In python there are different types of numbers we can use

# Integers

# Integer numbers (e.g. 2, 4, 20) have type int
myEpicInteger = 420

# If we check the type of this variable (epicInteger), we see it's an int
# type is another built in method (like print) that you can use by default
# we pass the result of type() into print() so we can see it on the screen
print(type(myEpicInteger))

# Floats
# floats are basically fractional numbers (decimals)
myCoolFloat = 4.2069

# again we can check the type of this variable and we see it's a float
print(type(myCoolFloat))

# you can use all the basic calculator operations on variables
# addition
num1 = 10
num2 = 20
result = num1 + num2
print(result)

# subtraction
num1 = 100
num2 = 50
result = num1 - num2
print(result)

# multiplication
num1 = 2
num2 = 2
result = num1 * num2
print(result)

# floating point division
num1 = 8
num2 = 4
result = num1 / num2
print(result)

# rounded division
num1 = 10
num2 = 3
result = num1 // num2
print(result)

#  exponents (ex 2^2)
num1 = 2
num2 = 2
result = num1 ** num2
print(result)

# modulo (gets the remainder after dividing)
num1 = 8
num2 = 2
result = num1 % num2 # gives 0 because 8 divides evenly into 2
print(result)

# another example
num1 = 8
num1 = 3 
result = num1 % num2 # gives 1 because 1 remains after dividing 8 by 3
print(result)


# HOMEWORK
# create two variables, one to store your age and one to store your height in feet (canadians get fucked)
# print your age divided by your height

# your height should be a float
# for example if you are 6ft 4in your height would be 6.33 (To get the fractional part, you divide the inches by 12. e.x. 4/12=0.33)