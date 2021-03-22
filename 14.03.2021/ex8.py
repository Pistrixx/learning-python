# new string using for

message = input("Enter your message: ")
new_message = ""
VOWELS = "aeiouy"

print()
for letter in message:
    if letter.lower() not in VOWELS:  # only lower case
        new_message += letter
        print("New string:", new_message)
print("Your message without vowels:", new_message)
