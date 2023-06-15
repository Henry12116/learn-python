# This lesson introduces the concept of modules and packages in Python.

# Modules are Python files that contain Python code (functions, classes, variables, etc). They are used to organize
# code into logical groups. For example, you could have a module called
# "mathematics" that contains functions for performing mathematical operations.
# To create a module, you create a file with a .py extension and add Python

# Packages are a collection of modules. For example, the "mathematics" module
# could be part of a package called "science" that contains other modules such
# as "physics" and "chemistry". You can use other peoples packages by installing
# them using the pip command. You can also create your own packages.
# To create a package, you create a folder and add a __init__.py file to it. From there,
# you can add modules to the package by creating Python files in the folder.

# Together modules and packages are used to organize code into logical groups
# and to make it easier to reuse code across multiple projects.

# Below is some excellent reading material on modules and packages:
# https://realpython.com/python-modules-packages/


# Next, check out example_pkg and example_usage.py to see this stuff in action.


# Homework
# Create a package called science that contains the following modules:
# mathematics.py, physics.py, and chemistry.py
# Each module should contain at least 4 functions that perform calculations
# mathematics.py - adding, subtracting, multiplying, and dividing
# physics.py - calculating force, acceleration, mass, and velocity
# chemistry.py - calculating molarity, moles, liters, and molecular weight
# Create a file called main.py that imports the science package and uses the functions, you can input what ever values you want,
# just make sure every function is used at least once.

# physics help
# force = mass times acceleration
# acceleration = force divided by mass
# mass = force divided by acceleration
# velocity = distance divided by time

# chemistry help
# molarity = moles divided by liters
# moles = molarity times liters
# liters = moles divided by molarity
# molecular weight = grams divided by moles
