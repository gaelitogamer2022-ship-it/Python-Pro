palabra = input("Ingresa una palabra: ")
vocales = ["a","e","i","o","u"]
palabra_letras = []
vocales_en_palabra = 0

for i in range(len(palabra)):
    palabra_letras.append(palabra[i])

for letra in palabra_letras: 
    if letra.lower() in vocales:
        vocales_en_palabra += 1

print("El número de vocales de esa palabra es:", vocales_en_palabra)
