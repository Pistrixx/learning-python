scores = []

choice = None
while choice != "0":

    print(
        """
        Scores 2.0
        
        0 - exit
        1 - show scores
        2 - add score
        """
    )

    choice = input("Choice: ")
    print()

    if choice == "0":
        print("The end.")

    elif choice == "1":
        print("Scores\n")
        print("PLAYER\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    elif choice == "2":
        name = input("Player's name: ")
        score = int(input("Player's score: "))
        entry = (score, name)  # sort by score
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]  # keep only 5 highest scores

    else:
        print("Unknown choice.")
