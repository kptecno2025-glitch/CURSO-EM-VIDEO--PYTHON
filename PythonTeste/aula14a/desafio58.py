from random import randint
pc = randint(0 , 10)
print('Vou pensar em um numero entre 0 e 10')
player = int(input('Digite um numero de 0 a 10: '))
tentativas = 0
while player != pc:
    print('Você errou! TENTE NOVAMENTE!')
    player = int(input('Digite um numero de 0 a 10: '))
    tentativas += 1
if player == pc:
    print('PARABENS VOCÊ GANHOU!')
    if tentativas <= 1:
        print(f'Você precisou de {tentativas} tentativa pra acertar')
    elif tentativas > 10:
        print(f'Mas... você precisou de {tentativas} tentativas para acertar')
    else:
        print(f'Você precisou de {tentativas} tentativas para acertar')
