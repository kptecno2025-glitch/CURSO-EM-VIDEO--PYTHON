nome = str(input('digite seu nome comleto: ')).strip()
print('Analisando seu nome...')
print('seu nome em maiusculo é {}'.format(nome.upper()))
print(f'seu nome em minusculo é {nome.lower()}')
print(f'seu nome tem {len(nome)-nome.count(' ')} letras')
#print(f'seu primeiro nome tem {len(nome.split()[0])} letras')
print(f'seu primeiro nome tem {nome.find(' ')} letras')


