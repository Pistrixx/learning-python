import random

WORDS = ("python", "easy", "complicated", "answer")
word = random.choice(WORDS)
correct = word

jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("Guess the word:", jumble)
guess = input("Your answer: ")

while guess != correct and guess != "":
    print("Try again!")
    guess = input("Your answer: ")

if guess == correct:
    print("Good guess!")