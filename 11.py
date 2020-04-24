from random import randint

jogos = []

pergunta = int(input('Quantos jogos você quer que sejam gerados?: '))

for gerar in range(pergunta):
    lista_jogos = []
    jogos.append(lista_jogos)
    for x in range(0,6):
        x = randint(1,60)
        lista_jogos.append(x)


for l, linhas in enumerate(jogos):
    l += 1
    print(f'Jogo {l}{linhas}')