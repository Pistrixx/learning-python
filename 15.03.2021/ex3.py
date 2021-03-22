import random

WORDS = ("carnotaurus", "velociraptor")
word = random.choice(WORDS)
len = len(word)
counter = 0
if_appears = False

print("\nTry to guess the word in 5 tries. The length of my chosen word is", len)

while counter != 5:
    letter = input("Enter a letter: ")

    if letter in word:
        if_appears = True

    if if_appears:
        print("That letter appears in my word.")
    else:
        print("There's no such letter in my word.")

    if_appears = False
    counter += 1

guess = input("Guess the word now: ")

if guess == word:
    print("Correct!")
else:
    print("Not really.")
