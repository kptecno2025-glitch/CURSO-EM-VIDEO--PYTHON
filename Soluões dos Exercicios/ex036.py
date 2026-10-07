casa = float(input('Valor da casa: R$'))
salario = float(input('salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos', end='')
print(f' a prestação será de R${prestação:.2f}')
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')
