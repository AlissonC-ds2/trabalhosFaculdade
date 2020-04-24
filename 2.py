num = []

while True:
    x = int(input('Números: '))
    pergunta = input('Deseja continuar cadastrando?: ')
    if pergunta in 'Nn':
        break
    else:
        if x not in num:
            num.append(x)
        else:
            print('Você digitou um valor já existente, não vai ser cadastrado na lista')


num.sort()
print(num)