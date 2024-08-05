# for loops allows us to iterate over list of items
# here increment occurs automatically
for i in [0, 1, 2]:
    print("meow")

# we can Optimize the algorithm
for i in range(3):  # 3 will not included
    print("optimized Meow")

# we Can also write this in other way
print("meow\n" * 3, end="")

for _ in range(3):  # 3 will not included
    print("optimized Meow")

"""
And just to show you something else that's Pythonic-- this is not strictly necessary, but it's commonly done, there's a minor improvement we can make here, even if we're just meowing three times. And notice that even though I'm defining a variable i, I'm not ever using it. 
And it's kind of necessary logically, because Python, presumably, has to use something for counting. It has to know what it's iterating over. But there's this convention in Python where if you need a variable, just because the programming feature requires it to do some kind of counting or automatic updating, but you, the human, don't care about its value, a Pythonic improvement here would be to name that variable a single underscore. 
Just because it's not required, it doesn't change the correctness of the program, but it signals to yourself later, it signals to colleagues or teachers that are looking at your code, too, that yes, it's a variable, but you don't care about its name because you're not using it later, it's just necessary in order to use this feature, this loop in this case here. So just a minor improvement or change there. 
"""
