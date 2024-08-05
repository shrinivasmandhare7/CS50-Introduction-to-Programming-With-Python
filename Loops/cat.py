# Deliberately inducing infinite loop
while True:
    n = int(input("Enter the number"))
    if n < 0:
        continue  # continue to stay within the loop
    else:
        break  # break out of the recently begin loop
