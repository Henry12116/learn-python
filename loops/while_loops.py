# while loops continue to execute until a condition is False
# NOTE: You can press ctrl+c in the terminal to stop the program (if you make an infinite loop)

# if we want this to loop 10 times (think of current_index as where we currently are in the loop)
# for example:
current_index = 0
while current_index < 10:  # while current_index is less than 10
    print("current_index is: ", current_index)  # print the current_index
    current_index += 1  # this is the same as saying current_index = current_index + 1


# you can also use while loops to iterate over a list
# for example:
from random import randint

random_numbers = [randint(1, 10000) for i in range(100)]
current_index = 0
while current_index < len(random_numbers):
    print("current number in list is: ", random_numbers[current_index])
    current_index += 1  # this is the same as saying current_index = current_index + 1


# you can use a while loop to run something forever
# for example:
i = 0
while True:
    print(f"running forever {i}")

    i += 1
    if i == 42:
        print("just kidding, that could freeze your computer")
        break  # you can use break to stop the loop


# ight let's have some fun with while loops
# we're going to use something called pyautogui to move the mouse around

# to do this you need to pip
# open a new cmd or terminal window, and run the following command:
# pip install pyautogui
# you may need to use pip3 instead of pip
# close all terminals and cmd windows

# now you should be able to run the following python code:
import pyautogui as pg

# sweet we just imported pyautogui, we can use that to do a bunch of shit
# you can read more about pyautogui here:
# https://pyautogui.readthedocs.io/en/latest/

# let's get the position of our mouse
print(pg.position())

# okay cool... now lets print the position of our mouse every 10th of a second
from time import sleep

while True:
    print(pg.position())
    sleep(0.1)


# this can be very useful for finding the position of a specific element on the screen
# maybe you want to find the position of a button on a page
# you can start this loop, hover over the button, then stop the program once it's recorded it's position

# Homework
# Using a while loop and pyautogui, make the mouse infinitely move in a box shape
# the box can be any size you want, but the mouse should move as follows:
# top left -> top right -> bottom right -> bottom left -> (repeat)

# Again you can use ctrl+c to stop the program.
