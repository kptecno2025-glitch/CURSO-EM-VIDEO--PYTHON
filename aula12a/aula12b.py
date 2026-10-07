nome = str(input('Qual seu nome? '))
if nome == 'Kauã':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('QUE NOME BASICO')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Um dos piores nomes feminino')
else:
    print('BETINHA')
print(f'Tenha um bom dia {nome}')
