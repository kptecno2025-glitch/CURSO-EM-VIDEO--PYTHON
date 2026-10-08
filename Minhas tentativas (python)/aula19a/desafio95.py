#CORRIGIDO DEPOIS DE ASSISTIR A RESOLUÇÃO
time = list()
jogador = {}
partida = []
while True:
    jogador.clear()
    jogador['nome']=str(input('Nome do jogador: '))
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    total = 0
    for c in range(0, part):
        gols = int(input(f'Quantos gols na partida {c+1}? '))
        partida.append(gols)
    jogador['gols'] = partida.copy()
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    partida.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999) para parar: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com codigo {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate (time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('--'*40)
print('<< VOLTE SEMPRE >>')

