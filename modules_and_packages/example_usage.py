# this module uses what we defined in example_pkg

# import the contents of example_pkg
from example_pkg import example_module1, example_module2

person = example_module1.Person("John")
example_module2.greeting(person.name)
example_module2.farewell(person.name)

# Example module 1 contains a class called Person
# Example module 2 contains two functions called greeting and farewell

# We use example_module 1 to create a Person object
# We use example_module 2 to call the greeting and farewell functions using the Person's name


# You can also use aliases when importing modules and packages
# This is useful when you want to import two modules that have the same name, or have long names
from example_pkg import example_module1 as em1, example_module2 as em2

person = em1.Person("John")
em2.greeting(person.name)
em2.farewell(person.name)

# This does the same thing as the previous example, but we use aliases to make the code easier to read
