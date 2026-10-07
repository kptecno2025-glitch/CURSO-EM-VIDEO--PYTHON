#FICOU INCOMPLETO
time = list()
jogador = {}
while True:
    jogador['nome']=str(input('Nome do jogador: '))
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    total = 0
    partida = []
    for c in range(0, part):
        gols = int(input(f'Quantos gols na partida {c}? '))
        partida.append(gols)
    jogador['gols'] = partida.copy()
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    partida.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {gols} partidas.')
for c, v in enumerate(jogador['gols']):
    print(f'    => Na partida {c}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')