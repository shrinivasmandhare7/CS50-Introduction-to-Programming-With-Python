# try below code
try:
    num = int(input("Please Enter a number"))
    # if something goes wrong execute the below Code
except ValueError:  # here ValueError is the Type of the Error
    print("######Please Enter a valid number")

print(f"num is {num}")

"""
 Just as a value error refers to that-- the value of some variable, the value that someone has 
 typed in is incorrect.
 NameError tends to refer to your code, like you're doing something with the name of a variable that 
 you shouldn't. 
"""
"""
What's happening here boils down to order of operations. Let me come back to the code here and recall 
that any time we've discussed the assignment operator, the single equal sign, that copies a value from
the right to the left. But consider for a moment at what point something is going wrong. 
Well, the input function is probably working just fine because we've used that a lot now to get users'
input. It always returns a string or a stir in Python. But what could be going wrong? Well, if I'm passing that string to the int function as its argument, it's probably the int's function that's erroring. 
And, indeed, if you think back earlier when we had the value error, it was, in fact, the int function that did not like, quote unquote, "cat" as input. So this is all to say that this portion of my code highlighted now to the right of the equal sign, that's the code that's creating a problem. That's the code that was creating a value error. 
And in this case, we're catching the value error. But because the value error is happening on the right of the equal sign, there's no value being copied to the left. The error is interrupting that whole process. So even though we see x equals dot dot dot on line two, the portion of that line to the left of the equal sign isn't getting evaluated, ultimately, because the value error is happening too soon. 
And so when we finally get down to line six, even though it looked like I was defining on line two--
and I would have defined x on line two if all had gone well-- we didn't get to the part where the value
is copied from right to left because the value error happened first. So this code is just incorrect now. So how do I go about solving something like this? 
"""
# the solution is that to use else (i.e.nothing goes wrong execute the code or if tried and Succeeds)
try:
    x = int(input("Enter X"))
except ValueError:
    print("Something went wrong")
else:
    print(x)
