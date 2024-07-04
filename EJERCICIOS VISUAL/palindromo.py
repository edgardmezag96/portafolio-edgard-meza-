def es_un_palindromo():
    
    print("Por favor, ingresa una palabra:")
    palabra = input()
    palabra_invertida = ""

    tamano = len(palabra)

    for x in range(tamano - 1, -1, -1):
        palabra_invertida += palabra[x]
    if palabra == palabra_invertida:
        print(f"'{palabra}' es un palíndromo.")
    else:
        print(f"'{palabra}' no es un palíndromo.")

es_un_palindromo()
