word = input("Enter a word")
vowels = ["a","e","i","o","u"]
word_letters = []
vowels_in_word = 0

for i in range(len(word)):
    word_letters.append(word[i])

for letter in word_letters:
    if letter.lower() in vowels:
        vowels_in_word += 1

print("The number of vowels in this word is", vowels_in_word)