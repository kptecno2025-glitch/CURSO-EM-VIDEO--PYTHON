from random import randint
v = 0
while True:
    player = int(input('Diga um valor: '))
    pc = randint(0, 10)
    total = player + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ìmpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {player} e o computador jogou {pc}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')

