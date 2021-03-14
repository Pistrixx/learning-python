# ex1
import random

print("Random quote of the day:")
number = random.randint(1, 5)

if number == 1:
    print("Yesterday is history, tomorrow is mystery but today is a gift that's why it's called the present.")
elif number == 2:
    print("This time… I hope for you these will be flowers of hope that never die.")
elif number == 3:
    print("It is time for you to look inward, and start asking yourself the big questions. Who are you? And what do "
          "you want?")
elif number == 4:
    print("Believe it!")
elif number == 5:
    print(
        "Defenders of Tyria! When Zhaitan rose from slumber, the dragon found a long-dead nation and claimed it. The "
        "dragon expected the rest of Tyria to be as easily conquered. But we live, and we breathe, and we fight! "
        "Together — charr and human, Priory and Vigil, all races and all paths of life; we stand against Zhaitan. The "
        "dragon wants us to be afraid because fear will tear us apart. Fear will destroy us! But I tell you this — I "
        "am not afraid! I may die, but I will never kneel! Did you feel that? It is the dragon who is afraid! To "
        "Arah, and victory!")

# ======================================================================================================================
# ex2
first_side = 0
second_side = 0
counter = 0

while counter < 100:
    side = random.randint(0, 1)
    if side == 0:
        first_side += 1
    else:
        second_side += 1
    counter += 1

print("\nFirst side:", first_side, ", second side:", second_side)

# ======================================================================================================================
# ex3
print("\nComputer will try to guess your number.")
your_number = int(input("Chose your number between 1 and 100: "))
computer_number = random.randint(1, 100)
i = 0

while computer_number != your_number:
    i += 1
    if computer_number > your_number:
        print("Too big:", computer_number)
        computer_number = random.randint(1, computer_number)
    elif computer_number < your_number:
        print("Too small:", computer_number)
        computer_number = random.randint(computer_number, 100)

print("Your number is", computer_number)
print("Computer guessed your number in", i, "tries")
