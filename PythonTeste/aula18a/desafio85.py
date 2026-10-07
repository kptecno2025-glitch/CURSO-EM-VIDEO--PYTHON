numeros = [[],[]]

for c in range(0,7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    elif valor % 2 == 1:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')