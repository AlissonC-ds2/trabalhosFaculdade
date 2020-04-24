expressao = input('Digite uma expressao númerica com ou sem parênteses: ')
print(expressao)


if '(' in expressao and ')' in expressao:
    print('parenteses fechado')
elif '(' in expressao and ')' not in expressao:
    print('parenteses em aberto')
else:
    print('expressao númerica sem parenteses')