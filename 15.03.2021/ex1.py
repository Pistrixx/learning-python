first = int(input("Enter the first number: "))
second = int(input("Enter the last number: "))
step = int(input("Set the gap: "))

for i in range(first, second, step):
    print(i, end=" ")
