# Welcome to Python!
# This is how you write a single line comment (start the line with a hashtag)

# Comments are useful for documenting code (i have shit memory, so I use comments often to remember wtf I was doing)

"""
You can also write multi line comment as well! Simply
open three quotation marks and bam

you're writing a multi line comment
"""

# There are two main ways that you can run python code
# 1. Directly writing python in the interpreter ex:
#   C:\Users\Hanky>python
#   Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
#   Type "help", "copyright", "credits" or "license" for more information.
#   >>> print("Hello World")
#   "Hello World"

# 2. Telling the interpreter which file to run ex:
#   C:\Users\Hanky>python my_script.py
#   Hello World

# When should I type my code directly in the interpreter vs saving it to a file?
#   If you are only running a small amount of code (I would say 5 lines maximum) then you can run your code directly in the interpreter.
#   When your code starts to get long, it can be difficult to manage only using the interpreter, thus it makes sense to save your code to a file, and then run that file.


# Our first program..... "Hello World"
#   Since there is only one line of code in this program, let's run this directly in the interpreter
#   1. From your command line (CMD on Windows or Terminal on Mac) type "python" ex:
#       C:\Users\Hanky>python
#   2. This should open the python interpreter, it will look like this:
#       Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
#       Type "help", "copyright", "credits" or "license" for more information.
#       >>>
#   3. type print("hello world") and hit enter. If everything worked, you should see "hello world" under the line you just typed

# you can use the print function to print out any string you want to the terminal
# this is very helpful for showing you what your program is doing as it is executing


# Homework: Try to run this code using the second method I showed above. (Tell the interpreter you want to run intro.py)
print("hello world 2: electric bugaloo")
