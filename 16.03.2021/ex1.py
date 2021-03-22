# lists
inventory = ()  # empty tuple

if not inventory:  # if inv is empty
    print("\nYour inventory is empty")

input("\nContinue...")

inventory = ["sword",
             "armor",
             "shield",
             "healing potion"]

print("List of your equipment:")
for item in inventory:
    print(item)

input("\nContinue...")

chest = ["gold", "gems"]
print("You found a chest! It contains:")
print(chest)
print("Let's add it to your inventory.")
inventory += chest
print("Now, take a look at your inventory: ")
print(inventory)

input("\nContinue...")

print("You exchange your sword for a crossbow.")
inventory[0] = "crossbow"
print("Your inventory: ")
print(inventory)

input("\nContinue...")

print("You use your gold and gems to buy tarot cards.")
inventory[4:6] = ["tarot cards"]
print("Your inventory: ")
print(inventory)

input("\nContinue...")

print("Your shield has been destroyed in a battle.")
del inventory[2]
print("Your inventory: ")
print(inventory)

input("\nContinue...")

print("Your crossbow and shield have been stolen!")
del inventory[:2]  # [0:2]
print("Your inventory: ")
print(inventory)
