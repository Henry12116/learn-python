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
print("10+20=", result)

# subtraction
num1 = 100
num2 = 50
result = num1 - num2
print("100-50=", result)

# multiplication
num1 = 2
num2 = 2
result = num1 * num2
print("2x2=", result)

# floating point division
num1 = 8
num2 = 4
result = num1 / num2
print("8/4=", result)

# rounded division
num1 = 10
num2 = 3
result = num1 // num2
print("10//3=", result)

# exponents (ex 2^2)
num1 = 2
num2 = 2
result = num1 ** num2
print("2^2=", result)

# modulo (gets the remainder after dividing)
num1 = 8
num2 = 2
result = num1 % num2 # gives 0 because 8 divides evenly into 2
print("8%2=", result)

# another example
num1 = 8
num1 = 3 
result = num1 % num2 # gives 1 because 1 remains after dividing 8 by 3
print("8%3=", result)

# lastly you can convert floats into integers and integers into floats by doing something called "type casting"
# for example say I have an integer
x = 2

# If I want to convert this into a float, I can simply call float()
y = float(x) # sets y equal to 2.0

# If I want to convert this back into an integer, I can call int()
z = int(y) # sets z equal to 2


# HOMEWORK
# create two variables, one to store your age and one to store your height in feet (canadians get fucked)
# print your age divided by your height

# your height should be a float
# for example if you are 6ft 4in your height would be 6.33ft (To get the fractional part, you divide the inches by 12. e.x. 4/12=0.33)

#more hw
age=19
height_in_feet=5
value1=9/12
height_in_feet + value1
number1=5.75
age/number1
#result 3.3043478260869565