# list's methods

scores = []
choice = None

while choice != "0":
    print(
        """
        Scores

        0 - exit
        1 - show score
        2 - add score
        3 - delete score
        4 - sort scores
        """
    )

    choice = input("Choice: ")
    print()

    if choice == "0":
        print("The end.")

    elif choice == "1":
        print("Scores")
        for score in scores:
            print(score)

    elif choice == "2":
        score = int(input("Enter your score: "))
        scores.append(score)

    elif choice == "3":
        score = int(input("Enter a score to remove: "))
        if score in scores:
            scores.remove(score)  # del bases on position, remove bases on value
        else:
            print(score, "does not exist.")

    elif choice == "4":
        scores.sort(reverse=True)  # from highest to lowest

    else:
        print("Unknown choice.")
