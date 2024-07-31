name=input('What is your Name ?')
# string Methods

name=name.strip() #Removes the WhiteSpaces from str
name=name.capitalize() # capitalize the first character in first string
name=name.title() #titleCase
print("Your Name is",name)

# We Can Chain this functions 
surname=input('Your Surname').strip().title() 
# the Execution Will be like 
# input() function will be executed first then it will be return value to strip() method that will be
# act as input strip() will return some value and then is will be used as input to title()

firstName, lastName=name.split(' ')
print(firstName)


