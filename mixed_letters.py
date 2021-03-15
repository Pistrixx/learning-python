import random

WORDS = ("python", "easy", "complicated", "answer")
HINTS = ("your favourite programming language",
         "not complicated",
         "not easy",
         "your response")
tries = 0

#word = random.choice(WORDS)
number = random.randint(0, len(WORDS)-1)
word = WORDS[number]
correct = word
hint = None

jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("Guess the word:", jumble)
guess = input("Your answer: ")
tries += 1

while guess != correct and guess != "":

    if tries >= 5:
        print("You seem to be stuck... need a hint?")
        hint = input("y/n: ")
        if hint == "y":
            print("There goes your hint.")
            print(HINTS[number])
        else:
            print("Let's continue without hints then.")

    print("Try again!")
    guess = input("Your answer: ")
    tries += 1

if guess == correct:
    print("Good guess!")

if hint == "n" and tries >= 5:
    print("Bonus point for not taking hints!")
