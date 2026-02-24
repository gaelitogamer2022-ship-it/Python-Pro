meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Aterrador, siniestro",
            "AGGRO": "Ponerse agresivo o enojado",
            "TRONKI": "Situación o reacción exagerada"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    if word == "CRINGE":
        print(meme_dict["CRINGE"])
    elif word == "LOL":
        print(meme_dict["LOL"])
    if word == "LOL":
        print(meme_dict["LOL"])
    elif word == "ROFL":
        print(meme_dict["ROFL"])
    if word == "SHEESH":
        print(meme_dict["SHEESH"])
    elif word == "CREEPY":
        print(meme_dict["CREEPY"])
    if word == "AGGRO":
        print(meme_dict["AGGRO"])
    elif word == "TRONKI":
        print(meme_dict["TRONKI"])
else:
    print("No tenemos la palabra indicada en nuestra lista")
