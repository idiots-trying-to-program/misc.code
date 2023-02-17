import math
print("pythag calc. 1. calculate hypotenuse\n2. calculate any other side")
e = int(input())
if e == 1:
    print("enter a and b")
    a = int(input())
    b = int(input())
    print(math.sqrt((a*a)-(b*b)))
if e == 2:
    print("enter hypotenuse then other side")
    a = int(input())
    b = int(input())
    print(math.sqrt((a*a)-(b*b)))
