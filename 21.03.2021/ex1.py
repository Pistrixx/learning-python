import random

WORDS = ["A", "B", "C", "D", "E", "F"]
used = []

while WORDS:
    word = random.choice(WORDS)
    used.append(word)
    WORDS.remove(word)

print(used)
