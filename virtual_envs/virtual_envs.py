# Up until now, we have been installing packages globally on your machine. This is fine for getting started, but it is not a good practice.

# The best practice is to use something called a virtual environment.

# What is a virtual environment?
# A virtual environment allows you to create an isolated environment for your project.
# This is useful when you want to use different versions of Python or different versions of packages for different projects.

# In a real world scenario, you will never simply pip instsall packages. This would install the packages globally on your machine.

# Instead, you would create a virtual environment for your project, and then install the packages in the virtual environment.

# Let's give this a try
# First, we need to install a package called virtualenv
# pip install virtualenv

# Next, we need to create a virtual environment
# virtualenv virtual_envs_lesson

# This will create a virtual environment called virtual_envs_lesson in the current directory.
# You can name the virtual environment whatever you want, but it is best practice to name it something that makes sense for your project.

# Next, we need to activate the virtual environment
# On Windows, run the following command:
# virtual_envs_lesson\Scripts\activate.bat

# On Mac/Linux, run the following command:
# source virtual_envs_lesson/bin/activate

# You should see (virtual_envs_lesson) at the beginning of your command prompt. This means you are in the virtual environment.

# You can deactivate the virtual environment by running the following command:
# deactivate

# Now that we have a virtual environment, let's install some packages
# pip install pandas
# pip install numpy
# pip install flask

# Now, let's create a requirements.txt file
# pip freeze > requirements.txt

# This is useful because it allows others to install all of the packages (dependencies) in the requirements.txt file with one command
# pip install -r requirements.txt

# So say you were another developer and wanted to open our project? Once you had our code, you could create a virtual environment, and then install all of the dependencies with one command.


# Homework
# create a second virtual environment, name it what ever you want
# activate the virtual environment
# install the requests package
# create a requirements.txt file
# deactivate the virtual environment

