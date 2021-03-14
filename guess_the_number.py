import random

print("Try to guess the number between 0 and 100.")

number = random.randint(0, 100)
your_number = int(input("Chose the number: "))
tries = 0
i = 20  # how many tries are left

while your_number != number:
    if your_number > number:
        print("Your number is too high.")
        i -= 1
        tries += 1
        if i == 0:
            break
        else:
            print("Remaining number of tries:", i)
    else:
        print("Your number is too low.")
        i -= 1
        tries += 1
        if i == 0:
            break
        else:
            print("Remaining number of tries:", i)
    your_number = int(input("Chose another number: "))

if i == 0:
    print("You lost!")
else:
    print("Your number is correct!")
    print("Tries counter:", tries)
