salario = float(input('Salario do funcionario: '))
novo = salario + (salario * 0.10)
min = salario + (salario * 0.15)
if salario >= 1250:
    print(f'Seu aumento R${novo:.2f}')
else:
    print(f'Seu aumento R${min:.2f}')