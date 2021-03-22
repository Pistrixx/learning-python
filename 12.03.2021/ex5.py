import random

print("Bedzie bitka")
health = 20
damage = 0
enemies = 0
while health > 0:
    damage = random.randint(1, 5)
    health = health - damage
    enemies = enemies + 1
    print("Wartosc ataku:", damage, ", zdrowie:", health, ", liczba pokonanych:", enemies)
