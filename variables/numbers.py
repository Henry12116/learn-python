# In python there are different types of numbers we can use

# Integers

# Integer numbers (e.g. 2, 4, 20) have type int
myEpicInteger = 420

# If we check the type of this variable (epicInteger), we see it's an int
# type is another built in method (like print) that you can use by default
type(myEpicInteger)

# Floats
# floats are basically fractional numbers (decimals)
myCoolFloat = 4.2069

# again we can check the type of this variable and we see it's a float
type(myCoolFloat)

# you can use all the basic calculator operations on variables
# addition
num1 = 10
num2 = 20
result = num1 + num2

# what's going on here?
print("{n1}+{n2}={r}".format(n1=num1, n2=num2, r=result))

# here i am cwafting a string by formatting it with variables
# first i create the format I want for my string, for this addition example, I want to show something like: x+y=z so i write:
" + = "
# i then inject the variables I want into said string by passing them to format
"{n1}+{n2}={r}".format(n1=num1, n2=num2, r=result)
# lastly i pass the result of this to print, so it appears on the screen
print("{n1}+{n2}={r}".format(n1=num1, n2=num2, r=result))


# subtraction
num1 = 100
num2 = 50
result = num1 - num2
print("{num1}-{num2}={result}".format(num1, num2, result))

# multiplication
num1 = 2
num2 = 2
result = num1 * num2
print("{num1}*{num2}={result}".format(num1, num2, result))

# floating point division
num1 = 8
num2 = 4
result = num1 / num2
print("{num1}/{num2}={result}".format(num1, num2, result))

# rounded division
num1 = 10
num2 = 3
result = num1 // num2
print("{num1}//{num2}={result}".format(num1, num2, result))

#  exponents (ex 2^2)
num1 = 2
num2 = 2
result = num1 ** num2
print("{num1}**{num2}={result}".format(num1, num2, result))

# modulo (gets the remainder after dividing)
num1 = 8
num2 = 2
result = num1 % num2 # gives 0 because 8 divides evenly into 2
print("{num1}%{num2}={result}".format(num1, num2, result))

# another example
num1 = 8
num1 = 3 
result = num1 % num2 # gives 1 because 1 remains after dividing 8 by 3
print("{num1}%{num2}={result}".format(num1, num2, result))


# HOMEWORK
# create two variables, one to store your age and one to store your height in feet (canadians get fucked)
# print your age divided by your height

# your height should be a float
# for example if you are 6ft 4in your height would be 6.33 (To get the fractional part, you divide the inches by 12. e.x. 4/12=0.33)