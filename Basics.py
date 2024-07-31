# input is a function which return the input fed by user in string Type
name=input('Whats your Name ?') 

# print is a function which print the argument passed to it ,Note it returns None
print("Your Name is",name,sep="--->") 
# Note  when you pass multiple arguments to print, it automatically inserts a space for you
# Also By Default Print add one Space Between arguments , to Override this we can add anything other in sep 


# what you can pass to a function and what those inputs are called, those are parameters. 
# When you actually use the function and pass in values inside of those parentheses, those inputs, 
# those values are arguments. So we're talking about the exact same thing-- parameters and arguments
# are effectively the same thing, but the terms you use from looking at the problem from different
# directions. When we're looking at what the function can take versus what you're actually passing 
# into the function. 


# Other Way of Doing this
surname=input("Whats Your Surname ?")

# By Default Print add New Line ,to Override this we add end as empty string
print('Hello',end='')
print(surname)


#Using Double cots in string
print('hello "Friend"')

#Other Way Which is more Elegant Way is to use Escape character
print("hello \"Friend\"")# Added backslash before inner double quote


# This is what we're going to call a format string or an F string, a relatively new feature of Python
# in the past few years that tells Python to actually format stuff in the string in a special way. 
print(f"hello {name}")