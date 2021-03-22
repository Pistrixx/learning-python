import random

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

print("First side:", first_side, ", second side:", second_side)
