salario = float(input('Qual é o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f}')