n = int(input('Dgite um numero: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mO numero {n} foi divisivel {tot} vezes')
if tot == 2: # O NUMERO É PRIMO SOMENTE QUANDO É DIVISIVEL DUAS VEZES
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO!')
