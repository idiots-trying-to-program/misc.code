print("Enter your username")
name = input()
print("Enter your password")
pw = input()
if name == "Hassan" and pw == "Lovemaaz123":
    then print("Welcome to your account syed")
while name != "Hassan" or pw != "Lovemaaz123":
    print("Incorrect username and/or password, try again")
    print("Enter your username")
    name = input()
    print("Enter your password")
    pw = input()
    if name == "Hassan" and pw == "Lovemaaz123":
        print("Welcome to your account syed")
print("Your name is,", name,"and your password is,",pw)
