numero = [[],[]]
for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    elif valor % 2 == 1:
        numero[1].append(valor)
print('-='*30)
numero[0].sort()
print(f'Os valores pares digitados foram: {numero[0]}')
numero[1].sort()
print(f'Os valores impares digitados foram: {numero[1]}')

