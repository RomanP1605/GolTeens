import random

k=0
for i in range(5):
    x = random.randint(1,9)
    y = random.randint(1,9)
    print(x, "*", y, "=")
    z = int(input(""))
    if x*y==z:
        print("correct")
        k=k+1
    else:
        print("incorrect")
    print(k)
