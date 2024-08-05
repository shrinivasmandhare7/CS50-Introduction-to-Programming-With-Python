"""
And so in my else, I could break out and return a value. So here, too, return is used to return values from functions. Break is used to break out of loops. But it turns out that return is sort of stronger than break.
It will not only break you out of a loop. It will also return a value for you. So it's doing two things for once, if you will.
"""


def main():
    x = getInput()
    y = getImprovedInput("Enter Y")
    print(x, y)


def getInput():
    while True:
        try:
            x = int(input("Enter a number"))
        except ValueError:
            print("Something went wrong")
        else:
            return x


# we Can improve this


def getImprovedInput(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # print("Something went wrong")
            pass
            """
            if you want to handle an exception in Python but you want to pass on doing anything with
            it-- so you want to catch it, but you essentially want to ignore it. You don't want to 
            print anything. You don't want to quit the program. You just want to silently ignore it, 
            like if you're talking in a room full of people and it's your turn to talk and you're 
            just like, pass. 
            """


main()
