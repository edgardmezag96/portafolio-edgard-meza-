
vocala = 0
vocale = 0
vocali = 0
vocalo = 0
vocalu = 0

print('Ingresa una frase: ')
frase = input()

x = len(frase)

for i in range(x):
    z = frase[i]
    
    if z == 'a' or z == 'A':
        vocala += 1
    if z == 'e' or z == 'E':
        vocale += 1
    if z == 'i' or z == 'I':
        vocali += 1
    if z == 'o' or z == 'O':
        vocalo += 1
    if z == 'u' or z == 'U':
        vocalu += 1

print('Total vocales:', vocala + vocale + vocali + vocalo + vocalu)