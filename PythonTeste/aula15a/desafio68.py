from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR')
player = s = cont = 0
while True:
    pc = randint(1, 10)
    player = int(input('Diga um valor: '))
    opção = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    total = player + pc
    print(f'Você jogou {player} e o computador jogou {pc}. total de {total}')
    if total % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    if opção == resultado:
        print('Você ganhou!')
        cont += 1
    else:
        print('Você perdeu!')
        break
print(f'Gamer Over! Você venceu {cont} vezes')
