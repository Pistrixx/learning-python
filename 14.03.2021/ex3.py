import random

print("Computer will try to guess your number.")
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
