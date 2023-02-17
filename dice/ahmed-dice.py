import random
def dice():
    print("dice roller")
    print(random.randint(1,6))
    print("go again?(Y/N)")
    e = input()
    e1 = e.lower()
    if e1 == "n":
        exit()
    if e1 == "y":
        dice()
dice()

