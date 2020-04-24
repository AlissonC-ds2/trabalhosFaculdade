lista = []
par = []
impar = []

while True:
    try:
        numeros = int(input('Digite um número: '))
        continuar = input('Continuar adicionando números? S/N: ')
        if continuar in 'Nn':
            break
        else:
            lista.append(numeros)
    except ValueError:
        print('Isso não é um número.')

for x in lista:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

print(f'Lista\n{lista}')
print(f'Numeros pares\n{par}')
print(f'Numeros impares\n{impar}')