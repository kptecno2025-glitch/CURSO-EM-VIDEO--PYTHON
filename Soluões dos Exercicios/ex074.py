from random import randint
n = (randint(1, 10),randint(1, 10),randint(1, 10),
     randint(1, 10),randint(1, 10))
print('Valores sorteados: ', end='')
for cont in n:
    print(f'{cont} ', end='')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')