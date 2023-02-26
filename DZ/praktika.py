import random

secret = random.randrange(1,101)
print(secret)
guess = 0
tries = 0

while guess != secret:
    guess = int(input("Type num"))
    tries+=1
    if secret > guess:
        print("too low")
    elif secret < guess:
        print("too high")
    else:
        print("correct")
print("Number of tries", tries)