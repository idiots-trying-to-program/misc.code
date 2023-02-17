# import math is a function is a package from the web that allows use to do many math calculations 
import math
# this print fuction allows use to chose what we wish to calculate in the calculator alone with the variable e to selct the mode they want 
print("pythag calculator.\n1. calc hypotenuse\n2. other side")
e = input()
# here the if statment does the calculations and the math.sqrt in the print function square root what is in the brakects 
if e == "1":
    print("enter your 2 numbers")
    a = int(input())
    b = int(input())
    print(math.sqrt((a*a)+(b*b)))
if e == "2":
    print("enter hypotenuse then other side")
    c = int(input())
    d = int(input())
    print(math.sqrt((c*c)-(d*d)))

# ahmed has helped be on this one as well
