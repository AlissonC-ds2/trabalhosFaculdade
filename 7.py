cadastro = []
pesados = []
leves = []
continuar = True

while continuar:
    dados = []
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    if len(cadastro) == 0:
        pesados = dados
        leves = dados
    else:
        if dados[1] > pesados[1]:
            pesados = dados
        if dados[1] < leves[1]:
            leves = dados
    print(dados)
    cadastro.append(dados)

    decisao = input('Deseja continuar? S/N')
    if decisao in 'Nn':
        continuar = False

print(len(cadastro))
print(cadastro)
print(pesados)
print(leves)


