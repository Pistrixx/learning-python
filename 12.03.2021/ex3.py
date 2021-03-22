# elif

import random

print("Wylosuje nastroj: ")
mood = random.randint(1, 3)
if mood == 1:
    print(":)")
elif mood == 2:
    print(":/")
elif mood == 3:
    print(":(")
else:
    print("Hmmm")
