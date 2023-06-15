# In python, input and output typically refers to reading and writing data to and from files.

# First, lets look at how we can read data from a file.

# We can read data from a file using the open function (this is built into python).

# The open function takes two arguments: the path to the file, and the mode.

# The mode is a string that tells Python what we want to do with the file. The mode can be one of the following:
# r: read mode
# w: write mode -> this will overwrite the contents of the file
# a: append mode -> this will add to the contents of the file
# r+: read and write mode
# w+: write and read mode
# a+: append and read mode

# Let's see some code!

with open("example.txt", "r") as f:
    contents = f.read()
    print(contents)

# What's going on here?
# We use the with keyword to open the file. This is because the with keyword will automatically close the file when we are done with it.
# "with" is called a context manager. You can read more about context managers here: https://book.pythontips.com/en/latest/context_managers.html

# We'll use the open function to open a file called example.txt in read mode. We alias the file as f.

# We'll then use the read method to read the contents of the file.

# We'll then print the contents of the file.

# If you get an error saying the file does not exist, make sure you are running this code from the input_and_output directory!

# Next, let's look at how we can write data to a file.
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# It's that simple!
# Again we use the with keyword to open the file because it automatically close the file when we are done with it.
# We call f.write to write the string "Hello, world!" to the file.
# Notice the file only contains the text "Hello, world!" now. This is because we opened the file in write mode, which overwrites the contents of the file.

# Finally, let's look at how we can append data to a file.
with open("example.txt", "a") as f:
    f.write("Hello, world again!")

# Notice we still call f.write, but this time we open the file in append mode, which appends the string to the end of the file.
# we can read the contents of the file again to see the changes
with open("example.txt", "r") as f:
    contents = f.read()
    print(contents)


# You can use other files types as well, such as json files or csv files. Additionally, there are exising packages that make it easier to read and write to these files.
# pandas is a great one

# Homework
# create a Person class with the following attributes: name, age, and city
# write a script that creates a list of 1000 random people
# write the list of people to a text file called people.txt
# I want the data to be formatted like this:
# -=-=-=-=-=-=-=-=-=-
# name: John Doe
# age: 25
# city: New York
# -=-=-=-=-=-=-=-=-=-
# name: Jane Doe
# age: 30
# city: Los Angeles
# -=-=-=-=-=-=-=-=-=-
# ...... and so on
