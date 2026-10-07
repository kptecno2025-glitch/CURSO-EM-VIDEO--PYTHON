n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite outro valor: '))
n4 = int(input('Digite outro valor: '))

tuple = (n1, n2, n3, n4)

print(f'Vc digitou os valores {tuple}')

print(f'O número 9 foi digitado {(tuple.count(9))} vezes')
if not 3 in tuple:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O número 3 apareceu na posição {tuple.index(3)+1}')

print(f'Os valores pares digitados foram:', end = ' ')
for c in tuple:
    if c % 2 == 0:
        print(c, end=' ')












