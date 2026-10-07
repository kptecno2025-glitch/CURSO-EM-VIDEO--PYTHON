import random
usu = int(input('Adivinhe qual numero eu pensei entre 1 a 5: '))
n1 = int('1')
n2 = int('2')
n3 = int('3')
n4 = int('4')
n5 = int('5')
lista = [n1, n2, n3, n4, n5]
escolhido = random.choice(lista)
print(escolhido)
if escolhido == usu:
    print('PARABENS!')
else:
    print('O computador venceu')

