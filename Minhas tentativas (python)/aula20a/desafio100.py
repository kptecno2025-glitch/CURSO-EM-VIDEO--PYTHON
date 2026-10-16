from time import sleep
from random import randint
numeros = []
def sorteio():
    print('Sorteando 5 valores da lista', end=' ')
    for i in range(5):
        numeros.append(randint(1, 10))
        print(numeros[i], end=' ')
        sleep(0.5)
    print('PRONTO!')

sorteio()

def somaPar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}')
somaPar()




