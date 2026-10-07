numeros = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in numeros:
        numeros.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opção == 'N':
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
