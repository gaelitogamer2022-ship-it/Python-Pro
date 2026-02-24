cadena = input("Ingresa una cadena de texto")
letras = []
for i in range(len(cadena)):
    letras.append(cadena[i])
if len(letras) >= 10:
    print(letras[:10], "...")
