import random
print('Vamos jogar Jokenpô, escolha:')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
escolha = int(input('Sua escolha: '))

opcoes = ['Pedra' , 'Papel', 'Tesoura']
jogador = opcoes[escolha - 1]
computador = random.choice(opcoes)

print(f'Vc escolheu: {jogador}')
print(f'Computador escolheu: {computador}')

if jogador == computador:
    print('Empate')
elif (jogador == 'Pedra' and computador == 'Tesoura') or (jogador == 'Papel' and computador == 'Pedra') or (jogador == 'Tesoura' and computador == 'Papel'):
    print('Você ganhou!')
else:
    print('Você perdeu!')

