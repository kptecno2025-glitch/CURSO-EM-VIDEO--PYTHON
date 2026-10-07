n = 0
cont = 0
soma = 0
print('Digite 999 pra parar')
while n != 999:
    n = int(input('Digite um numero: '))
    if n != 999:
        soma += n
        cont += 1
print(f'Você finalizou o programa com {cont} numeros digitados')
print(f'E a soma entre todos eles deu {soma}')