import random
import time
print("""*******************************

welcome to the guessing game

*******************************""")

guessing_number = random.randint(1,40)
left_over = 7
while True:
    input_from_user = int(input("please login your prediction:"))
    if guessing_number > input_from_user:
        print("we're checking the numbers.")
        time.sleep(1)
        print("please tell us bigger number")
        left_over -= 1
    elif guessing_number < input_from_user:
        print("we're checking the numbers.")
        time.sleep(1)
        print("please tell us smaller number")
        left_over -= 1
    else:
        print("we're checking the numbers.")
        time.sleep(1)
        print("Correct answer! \nNumber is: {}".format(guessing_number))
        break
    if left_over == 0:
        print("you dont have any prediction \nNumber is: {}".format(guessing_number))
        break

