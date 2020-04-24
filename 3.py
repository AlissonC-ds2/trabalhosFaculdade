num = []

for n in range(0, 5):
    i = int(input('numeros: '))

    if n == 0 or i > num[-1]:
        num.append(i)
    else:
        posicao = 0
        while posicao < len(num):
            if i <= num[posicao]:
                num.insert(posicao, i)
                break
            posicao += 1
print(num)