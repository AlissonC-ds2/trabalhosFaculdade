'''Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

alunos = list()
boletim = list()

while True:
    dados = list()

    aluno = input('Nome do aluno: ')
    nota1 = float(input('Primeira nota do aluno: '))
    nota2 = float(input('Segunda nota do aluno: '))
    media = (nota1 + nota2) / 2
    dados.append(aluno)
    dados.append(nota1)
    dados.append(nota2)
    alunos.append(dados)
    boletim.append(media)

    pergunta = input('Deseja continuar cadastrando?: ')
    if pergunta in 'Nn':
        break

for l, linhas in enumerate(alunos):
    print(l, f'Aluno: {linhas}',f'---------------------------------Média:{boletim[l]}', end=' ')
    print()

while True:
    perguntar = input('Deseja verificar a notas do aluno individualmente? S/N ')
    if perguntar in 'Nn':
        break
    else:
        escolha = int(input('Por favor digite o número do aluno: '))
        print(f'Notas do aluno: {alunos[escolha]}')