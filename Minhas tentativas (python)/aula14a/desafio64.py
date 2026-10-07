soma = 0
cont = 0
numero = 0
print('Digite 999 para encerrar o programa')
while numero != 999:
    numero = int(input('Digite um numero: '))
    if numero != 999:
        cont += 1
        soma += numero
print(f'A quantidade de numeros digitados foram {cont}')
print(f'A soma entre os numeros digitados foi {soma}')