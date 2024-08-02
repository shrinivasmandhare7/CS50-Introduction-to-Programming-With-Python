# > < >= <= == !=
# if the keyword which we use in python to ask the question like if age is greater than 18 then do this
# question is boolean expression means it has yes or no answer

x = int(input("Enter X"))
y = int(input("Enter Y"))

# keywords if elif else
if x > y:
    print("X is greater than Y")
elif x < y:
    print("X is Lesser than Y")
else:
    print("X is Equal to Y")


score = int(input("Score"))
if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score < 90:
    print("Grade B")
elif score >= 70 and score < 80:
    print("Grade C")
else:
    print("Grade F")

# We Can Simply the above code as follows,(Note that the same thing is not possible in C++)
# it is called as Chained Comparisons

if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <= score < 80:
    print("Grade C")
else:
    print("Grade F")


# we Can Optimize the algorithm
# Note that Each Conditions are mutually exclusive
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade F")


# if we have only if else we can use it in one line as
def isEven(num):
    return True if num % 2 == 0 else False


"""
Notice this value here is my Boolean expression. And it is going to evaluate to true or false. Is n 
divided by two having a remainder of zero or not? That is, by definition, a Boolean expression. It has
a yes/no answer, a true/false answer. Well, if your Boolean expression itself has a true or false 
answer, why are you asking a question in the first place? Why ask if? Why say else? 
Just return the value of your own Boolean expression. And perhaps the tightest version, the most 
succinct, and still readable, version of this code would be to delete this whole line, Pythonic 
though it is, and just return n modulo two equals equals zero. If it helps, let me add parentheses temporarily, because what's going to happen in parentheses will happen first. 
n divided by two either does or does not have a remainder of zero. If it does, the answer is true. 
If it doesn't, the answer is false. So just return the question, if you will. You don't need to wrap it, explicitly, with an if and an else. And in fact, because of order of operations, you don't even need the parentheses. So now this is perhaps the most elegant way to implement this same idea.
"""
