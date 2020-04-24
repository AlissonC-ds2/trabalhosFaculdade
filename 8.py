lista_num = []
par = []
impar = []

for x in range(0, 7):
    numeros = int(input('Digite um número: '))
    if numeros % 2 == 0:
        par.append(numeros)
    else:
        impar.append(numeros)

lista_num.append(sorted(par))
lista_num.append(sorted(impar))

print(lista_num)


