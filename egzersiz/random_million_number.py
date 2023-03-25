import random

while True:
    a = input("try something: ")
    a = a.upper()

    if a == "A":
        a = random.randint(1,999)
        b = random.randint(1,999)
        c = random.randint(1,999)
        print("{}.{}.{}".format(a,b,c))
    else:
        break