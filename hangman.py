import random

HANGMAN = (
    """
    ------
    |    |
    |
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
     ------
    |    |
    |    O
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
     ------
    |    |
    |    O
    |   -+-
    |
    |
    |
    |
    |
    ----------
    """,
    """
     ------
    |    |
    |    O
    |  /-+-
    |
    |
    |
    |
    |
    ----------
    """,
    """
     ------
    |    |
    |    O
    |  /-+-/
    |
    |
    |
    |
    |
    ----------
    """,
    """
     ------
    |    |
    |    O
    |  /-+-/
    |    |
    |
    |
    |
    |
    ----------
    """,
    """
     ------
    |    |
    |    O
    |  /-+-/
    |    |
    |   |
    |   |
    |
    |
    ----------
    """,
    """
     ------
    |    |
    |    O
    |  /-+-/
    |    |
    |   | |
    |   | |
    |
    |
    ----------
    """,
)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("PYTHON", "JAVA", "DATA", "SCIENCE")

word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

print("Welcome to the hangman game!")

while wrong < MAX_WRONG and so_far != word:

    print(HANGMAN[wrong])
    print("Used letters:\n", used)
    print("What you have guessed so far:\n", so_far)

    guess = input("Your letter: ")
    guess = guess.upper()

    while guess in used:
        print(guess, "has been already used.")
        guess = input("Your next letter: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("Good guess!")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("There's no such letter in the mysterious word.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("You lost!")
else:
    print("You guessed the word!")
    print("The word is:", word)
