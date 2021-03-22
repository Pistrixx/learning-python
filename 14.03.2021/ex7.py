# indexing

import random

word = "index"
print("\nThe word is: ", word)

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)  # random.randrange(5, -5)
    print("word[", position, "]\t", word[position])
