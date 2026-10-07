matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input('Digite um valor: '))
        matriz[linha][coluna] = valor
print(f'[  {matriz[0][0]}  ] [  {matriz[0][1]}  ] [  {matriz[0][2]}  ] ')
print(f'[  {matriz[1][0]}  ] [  {matriz[1][1]}  ] [  {matriz[1][2]}  ] ')
print(f'[  {matriz[2][0]}  ] [  {matriz[2][1]}  ] [  {matriz[2][2]}  ] ')
