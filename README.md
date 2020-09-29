# hierarchical_data

What this project is for
This application is a Django database, that uses a Hierarchical Data to create a database that has a tree like data structure. The goal is to be able to pull all relational data out of a single instance of data using a method such as data.get_ancestors().

How it works
This project utilizes a model type called Modified Preorder Tree Traversal, or MPTT. The goal of this project is to learn how to utilize this method of relational data management.


Dependencies required for this project
Python 3.8.2
django-mptt = "^0.11.0"

Poetry
Linux-based or Mac operating system
Bash or Zsh shell

Set-Up
Fork and clone the repo.
cd into your new directory, and run the command poetry install. This is going to install all of the dependecies required for the project.
now run poetry shell. This will create a virtual enviornment for your terminal. From here you can run commands off of a file called manage.py. This file holds all of the information for things such as running a server.
you can run the command python manage.py runserver to run the server. (Note that this particular project does not display anything on a webpage so it would display a blank webpage.) If you want to look at the relational data structure, do code . in the root folder to open it up in VS Code and you can view the data structure.
