from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 12)
if pc == 0: #pc jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('INVALIDO')
elif pc == 1: #pc jogou PAPEL
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    elif jogador == 0:
        print('COMPUTADOR VENCE')
    else:
        print('INVALIDO')
elif pc == 2: #pc jogou TESOURA
    if jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    else:
        print('INVALIDO')
