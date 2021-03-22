print("Petelka nieskonczona")
count = 0
while True:
    count = count + 1
    if count > 10:
        break
    if count == 5:
        continue
    print(count)
