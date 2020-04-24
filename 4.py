lista = []

while True:
    x = int(input('Digite um numero: '))
    p = input('Deseja continuar adicionando números? S/N: ')
    count = 0
    lista.append(x)
    if p in 'Nn':
        break
    else:
        for numero in lista:
            count += 1
    print(f'Foram digitados {count} numeros.')

if 5 in lista:
    print('O numero 5 está na lista.')
else:
    print('O numero 5 não esta na lista.')
lista.sort(reverse=True)
print(lista)