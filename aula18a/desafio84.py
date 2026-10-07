galera = list()
dados = list()
pesado = list()
leve = list()
while True:
    dados.append(str(input('Nome: ')))
    peso = float(input('Peso: '))
    if peso > 75:
        pesado.append(dados[0])
    elif peso < 75:
       leve.append(dados[0])
    galera.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo vc cadastrou {len(galera)} pessoas')
print(f'As pessoas mais pesadas são: {pesado}')
print(f'As pessoas mais leves são: {leve}')











