from operator import itemgetter
from random import randint
from time import sleep
jogadores = {}
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)

print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'   O {k} tirou {v}')
    sleep(1)

print('Ranking dos jogadores')
ranking = sorted(jogadores.items() ,
                 key=itemgetter(1),
                 reverse=True)
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

