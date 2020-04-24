matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

def mostar_matriz():
    print('-='*30)
    for linha in matriz:
        for item in linha:
            print('[  {}  ]'.format(item), end='')
        print()
    print('-='*30)

for i, valor in enumerate(matriz): # i = INDEX
    for j, valor in enumerate(matriz[i]): #j = Coluna
        print(j)
        matriz[i][j] = input('informe um valor para linha {} e coluna {}'.format(i,j))

        mostar_matriz()

