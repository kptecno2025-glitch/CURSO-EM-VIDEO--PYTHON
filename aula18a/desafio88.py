from random import randint
from time import sleep
lista = []
jogos = []
print('_'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('_'*30)
jogadas = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(jogadas):
    while len(lista) < 6:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '<BOA SORTE>', '-=' * 5)



