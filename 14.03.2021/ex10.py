# tuples

inventory = ()  # empty tuple

if not inventory:  # if inv is empty
    print("\nYour inventory is empty")

input("\nContinue...")

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

input("\nContinue...")

chest = ("gold", "gems")
print("You found a chest! It contains:")
print(chest)
print("Let's add it to your inventory.")
inventory += chest
print("Now, take a look at your inventory: ")
print(inventory)
