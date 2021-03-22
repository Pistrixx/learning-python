# cutting out strings

word = "pizza"
print(
    """\n
    0   1   2   3   4   5
    +---+---+---+---+---+
    | p   i   z   z   a |
    +---+---+---+---+---+
   -5  -4  -3  -2  -1
    """
)
print("Enter the beginning and ending index of the string 'pizza'.")

start = None  # false, null
while start != "":
    start = (input("Beginning: "))

    if start:  # if start has a value
        start = int(start)

        finish = int(input("Ending: "))

        print("word[", start, ":", finish, "] is", end=" ")
        print(word[start:finish])
    break
