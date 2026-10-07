    #RESOLUÇÃO DO CURSO EM VIDEO
from random import randint
from time import sleep
pc = randint(0, 5) #Faz o computador "PENSAR"
print('=-=' * 30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('=-=' * 30)
player = int(input('Em que numero eu pensei? ')) #Jogador tenta adivinhar
print('\033[33mPROCESSANDO...')
sleep(3)
if player == pc:
    print('\033[34mPARABENS! Você conseguiu me vencer!')
else:
    print(f'\033[31mGANHEI! Eu pensei no numero {pc} e não no {player}')

    #A FORMA COMO EU CHEGUEI NO RESULTADO
'''import random
print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')
numero = int(input('Em que numero eu pensei? '))
n1 = 0
n2 = 1
n3 = 2
n4 = 3
n5 = 4
n6 = 5
lista = [n1, n2, n3, n4, n5, n6]
escolhido = random.choice(lista)
print('Processando...')
if escolhido == numero:
    print('PARABENS!, Você conseguiu me vencer!')
else:
    print('VC PERDEU!')'''
