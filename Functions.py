# In Python, you have to define the function before you use it,
# to tackle this issue we can define main function which will see in  next step
def hello(to="World"):  # parametrized function
    print("Hello ", to)


name = input("Your name")
hello(name)  # passing the argument


def main():
    name = input("Your name")
    hello(name)  # passing the argument


main()

"""
1.Function Definitions:
Both functions, main and hello, are defined before the main function is executed. Python doesn't 
execute the function bodies at the point of definition; it only remembers their definitions.

2.Execution Order:
In the code, neither main nor hello is executed until they are explicitly called somewhere after their
definitions.
The function main calls hello only after both functions are defined.

3.No Immediate Execution:
When you define functions, Python doesn’t run any of the code inside them until the functions are called.
"""
