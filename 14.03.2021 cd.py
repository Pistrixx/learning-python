# for
word = input("Write a word: ")
print("Letters of your word:")
for letter in word:
    print(letter)

# ======================================================================================================================
# for + range()
print("\nCounting:")
for i in range(10):
    print(i, end=" ")

print("\nCounting every 5:")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\nCounting backwards:")
for i in range(10, 0, -1):
    print(i, end=" ")

# ======================================================================================================================
# len() + in
message = input("\n\nEnter your message: ")
print("Length of your message is", len(message))
print("Letter 'a'",)
if "a" in message:
    print("appeared.")
else:
    print("didn't appear.")

# ======================================================================================================================
# indexing
import random

word = "index"
print("\nThe word is: ", word)

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)  # random.randrange(5, -5)
    print("word[", position, "]\t", word[position])

# ======================================================================================================================
# new string using for
message = input("\nEnter your message: ")
new_message = ""
VOWELS = "aeiouy"

print()
for letter in message:
    if letter.lower() not in VOWELS:  # only lower case
        new_message += letter
        print("New string:", new_message)
print("Your message without vowels:", new_message)

# ======================================================================================================================
# cutting out strings
word = "pizza"
print(
    """\n
    0   1   2   3   4   5
    +---+---+---+---+---+
    | p   i   z   z   a |
    +---+---+---+---+---+
   -5  -4  -3  -2  -1
    """
)
print("Enter the beginning and ending index of the string 'pizza'.")

start = None  # false, null
while start != "":
    start = (input("Beginning: "))

    if start:  # if start has a value
        start = int(start)

        finish = int(input("Ending: "))

        print("word[", start, ":", finish, "] is", end=" ")
        print(word[start:finish])
    break

# ======================================================================================================================
# tuples
inventory = ()  # empty tuple

if not inventory:  # if inv is empty
    print("\nYour inventory is empty")

input("Continue...")

inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

print("Your inventory:")
print(inventory)

print("List of your equipment:")
for item in inventory:
    print(item)

print("Your inventory has", len(inventory), "elements.")

if "shield" in inventory and "armor" in inventory:
    print("You can protect yourself.")
else:
    print("You can't protect yourself!")

index = int(input("Enter the number of an element: "))
print("Number", index, "is", inventory[index])

start = int(input("Beginning: "))
finish = int(input("Ending: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("Continue...")

chest = ("gold", "gems")
print("You found a chest! It contains:")
print(chest)
print("Let's add it to your inventory.")
inventory += chest
print("Now, take a look at your inventory: ")
print(inventory)
