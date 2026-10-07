completa = []
pares = []
impares = []

while True:
    valor = int(input('Digite um valor: '))
    completa.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opção == 'N':
        break

print('-='*30)
print(f'A lista completa é {completa}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
