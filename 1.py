num = []

for x in range(5):
    x = int(input('numero: '))
    num.append(x)

maior = max(num)
menor = min(num)
maior_index = num.index(maior)
menor_index = num.index(menor)
print('Maior número: {}, está na posição {} da lista.\nMenor número: {}, está na posição {} da lista.'.format(maior,maior_index,menor,menor_index))
