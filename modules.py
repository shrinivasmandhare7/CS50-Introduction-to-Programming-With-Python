"""
This ability to share code with others, share code across your own projects. And it does so by way of
what it calls module. A module in Python is just a library that typically has one or more functions or
other features built into it.
eg: random,
"""

# The import keyword in Python allows you to import the contents of the functions from some module in
# Python.
import random  # import everything
from random import choice  # import specific choice
# And what this does effectively is it loads the function's name choice into my current namespace into
# the scope of the file I'm working in.

print(random.choice(["Heads", "Tails"]))
print(choice(["Heads", "Tails"]))
print(random.randint(1, 10))
