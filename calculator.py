# you can nest functions. You can put one function call that is the use of a function 
# inside of the use of another function so that the return value of the inner function becomes the 
# argument to or the input to the outer function.
x = float(input())
y = float(input())

print(round(x+y,2))
# Second argument is ndigits means round to nearest number of digits