word_dict = {
    "CRINGE": "Something exceptionally strange or embarrassing",
    "LOL": "A common response to something funny",
    "ROFL": "A response to a joke",
    "SHEESH": "Slight disapproval",
    "CREEPY": "Frightening, sinister",
    "AGGRO": "Becoming aggressive or angry"
}
word = input("Write a word you don't understand (with capital letters)")

if word in word_dict.keys():
    if word == "CRINGE":
        print(word_dict["CRINGE"])
    if word == "LOL":
        print(word_dict["LOL"])
    if word == "ROFL":
        print(word_dict["ROFL"])
    if word == "SHEESH":
        print(word_dict["SHEESH"])
    if word == "CREEPY":
        print(word_dict["CREEPY"])
    if word == "AGGRO":
        print(word_dict["AGGRO"])