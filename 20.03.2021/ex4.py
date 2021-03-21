# dictionaries
games = {
    "Doom": "1993",
    "Portal": "2007",
    "Guild Wars 2": "2012",
    "Super Mario Bros": "1985"
}

choice = None
while choice != "0":

    print(
        """
        Games

        0 - exit
        1 - find game
        2 - add a new game
        3 - modify game
        4 - delete game
        5 - show games
        """
    )

    choice = input("Choice: ")
    print()

    if choice == "0":
        print("The end.")

    elif choice == "1":
        term = input("Game: ")
        if term in games:
            year = games[term]
            print("\n", term, ", release date:", year)
        else:
            print(term, "does not exist in this dictionary.")

    elif choice == "2":
        term = input("Game: ")
        if term not in games:
            year = input("Release date: ")
            games[term] = year
            print("Game has been added.")
        else:
            print(term, "already exist in this dictionary.")

    elif choice == "3":
        term = input("Game to modify: ")
        if term in games:
            year = input("New release date: ")
            games[term] = year
            print("Year has been changed.")
        else:
            print(term, "does not exist in this dictionary, try adding it.")

    elif choice == "4":
        term = input("Game to delete: ")
        if term in games:
            del games[term]
            print(term, "has been deleted.")
        else:
            print("cannot delete", term, ", it does not exist in this dictionary.")

    elif choice == "5":
         print(games.items())

    else:
        print("Unknown choice.")
