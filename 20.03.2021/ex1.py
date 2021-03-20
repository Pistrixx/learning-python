# nested sequences
nested = ["one", ("two", "three"), ["four", "five", "six"]]
print(nested)

tab = [("A", 1000), ("B", 1500), ("C", 3000)]
print("\n" + str(tab))

print("\nfor:")
for i in tab:
    print(i)

print("\ndirectly:")
print(tab[1])

print("\nindexing and tuples:")
a_tab = tab[2]
print(a_tab)
print(a_tab[0])

print("\nthe same but directly:")
print(tab[2][0])  # list[tuple][tuple_element]

print("\nunpacking:")
letter, number = ("D", 175)
print(letter)
print(number)
