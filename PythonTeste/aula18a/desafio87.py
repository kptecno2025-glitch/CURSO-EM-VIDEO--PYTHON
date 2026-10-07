matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if valor % 2 == 0:
            pares += valor
        matriz[linha][coluna] = valor
print(f'[  {matriz[0][0]}  ] [  {matriz[0][1]}  ] [  {matriz[0][2]}  ] ')
print(f'[  {matriz[1][0]}  ] [  {matriz[1][1]}  ] [  {matriz[1][2]}  ] ')
print(f'[  {matriz[2][0]}  ] [  {matriz[2][1]}  ] [  {matriz[2][2]}  ] ')

print(f'A soma dos valores pares é {pares}')
coluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {coluna3}')
maiorL2 = max(matriz[1])
print(f'O maior valor da segunda linha é {maiorL2}')

