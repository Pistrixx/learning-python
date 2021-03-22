# or and not

print("Ekskluzywna siec")
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
