# character creator

stats = {
    "power": 0,
    "vitality": 0,
    "toughness": 0,
    "precision": 0
}

points = 30

choice = None
while choice != "0":

    print(
        """
        Character creator
        
        0 - exit
        1 - show stats
        2 - add points
        3 - remove points
        4 - show points
        """
    )

    choice = input("Choice: ")
    print()

    if choice == "0":
        print("The end.")

    elif choice == "1":
        for i in stats:
            print(i, "-", stats.get(i))

    elif choice == "2":
        attribute = input("Select attribute: ")
        if attribute in stats:
            how_many = int(input("How many points to add?: "))
            if how_many <= points:
                stats[attribute] = how_many
                points -= how_many
            else:
                print("Wrong amount of points! You have", points, "points to spend.")
        else:
            print("Wrong attribute!")

    elif choice == "3":
        attribute = input("Select attribute: ")
        if attribute in stats:
            how_many = int(input("How many points to remove?: "))
            if how_many <= stats[attribute]:
                stats[attribute] -= how_many
                points += how_many
            else:
                print("Wrong amount of points! You can remove up to", stats[attribute], "points.")
        else:
            print("Wrong attribute!")

    elif choice == "4":
        print("You have", points, "points to spend.")

    else:
        print("Unknown choice.")
