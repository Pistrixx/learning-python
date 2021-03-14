# random
import random
rand1 = random.randint(1, 6)
rand2 = random.randrange(6) + 1
total = rand1 + rand2
print("Wyrzuciles", rand1, "oraz", rand2, "oczek o sumie", total)

# ======================================================================================================================
# if
password = input("\nPodaj haslo: ")
if password == "okon":
    print("Dobre haslo")
    print("Maslo")
else:
    print("Zle haslo")

# ======================================================================================================================
# elif
"""import random"""
print("\nWylosuje nastroj: ")
mood = random.randint(1, 3)
if mood == 1:
    print(":)")
elif mood == 2:
    print(":/")
elif mood == 3:
    print(":(")
else:
    print("Hmmm")

# ======================================================================================================================
# while
print("\nA taki symulator")
response = ""
while response != "Nie":
    response = input("Nie ")
print("Ok")

# ======================================================================================================================
# symulator
print("\nBedzie bitka")
health = 20
damage = 0
enemies = 0
while health > 0:
    damage = random.randint(1, 5)
    health = health - damage
    enemies = enemies + 1
    print("Wartosc ataku:", damage, ", zdrowie:", health, ", liczba pokonanych:", enemies)

# ======================================================================================================================
# break/continue
print("\nPetelka nieskonczona")
count = 0
while True:
    count = count + 1
    if count > 10:
        break
    if count == 5:
        continue
    print(count)

# ======================================================================================================================
# or and not
print("\nEkskluzywna siec")
security = 0
username = ""
while not username:
    username = input("Uzytkownik: ")
password = ""
while not password:
    password = input("Haslo: ")
if username == "M.Dawson" and password == "sekret":
    print("Dawson")
    security = 5
if username == "gosc" or password == "gosc":
    print("Gosc")
    security = 1
else:
    print("Nieudana proba logowania")
