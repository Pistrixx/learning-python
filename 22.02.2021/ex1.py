# 'who's your dad?'

family = {
    "Bill Gates": None,
    "Steve Jobs": None,
    "Hans Zimmer": None,
    "Jeremy Soule": None
}

choice = None
while choice != "0":
    print(
        """
        Who's your dad?

        0 - exit
        1 - show pairs
        2 - add pair
        3 - remove pair
        4 - change pair
        5 - add son
        """
    )

    choice = input("Choice: ")
    print()

    if choice == "0":
        print("The end.")

    elif choice == "1":
        for i in family:
            print(i, "-", family.get(i))

    elif choice == "2":
        dad = input("Dad: ")
        if dad not in family:
            son = input("Son: ")
            family[dad] = son
            print("Pair has been added.")
        else:
            print(dad, "already exist.")

    elif choice == "3":
        dad = input("Pair (dad) to delete: ")
        if dad in family:
            del family[dad]
            print(dad, "has been deleted.")
        else:
            print("Cannot delete", dad, ", it does not exist.")

    elif choice == "4":
        dad = input("Chose a dad: ")
        dad2 = input("Chose a second dad to swap with the first dad: ")
        if dad and dad2 in family:
            temp = family[dad]
            family[dad] = family[dad2]
            family[dad2] = temp
            print("Dads has been swapped!")
        else:
            print("Cannot swap dads! They don't exist.")

    elif choice == "5":
        dad = input("Dad: ")
        if dad in family:
            son = input("Son: ")
            family[dad] = son
            print("Son has been added!")
        else:
            print("That dad doesn't exist!")

    else:
        print("Unknown choice.")
