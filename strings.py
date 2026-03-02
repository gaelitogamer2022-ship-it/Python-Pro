string = input("Enter a text string")

letters = []

for i in range(len(string)):
    letters.append(string[i])

if len(letters) >= 10:
    print(letters[:10], "...")