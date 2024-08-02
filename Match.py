# Compares multiple strings with if/elif/else
name = input("Your Name")

if name == "Shree" or name == "Aishwarya":
    print("Your Surname is Mandhare")
elif name == "Bhushan":
    print("Your Surname is Kinge")
elif name == "Raj":
    print("Your Surname is Rathod")
else:
    print("Dont Know your Surname")

# match is just like switch case in cpp note that we do not break statements here in python
match name:
    case "Shree" | "Aishwarya":
        print("Your Surname is Mandhare")
    case "Bhushan":
        print("Your Surname is Kinge")
    case "Raj":
        print("Your Surname is Rathod")
    case _:  # it's Like a default case in CPP
        print("Dont Know your Surname")
