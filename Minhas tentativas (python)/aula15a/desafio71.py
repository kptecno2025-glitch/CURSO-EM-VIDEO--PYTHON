print('='*30)
banco = 'BANCO CEV'
print(f'{banco:^30}')
print('='*30)

cedula = 50

valor = int(input('Que valor você que sacar? R$'))
while True:
    quant = valor // cedula
    resto = valor % cedula
    if quant > 0:
        print(f'{quant} cedula(s) de R${cedula}')
    valor = resto



    if cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 1
    else:
        break
