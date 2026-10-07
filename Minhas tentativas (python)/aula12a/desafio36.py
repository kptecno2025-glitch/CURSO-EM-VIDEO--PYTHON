casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salario do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
mensalidade = anos * 12
prestação = casa / mensalidade
emprestimo = salario * (30 / 100)
print(f'Prestação: R${prestação:.2f}')
if prestação > emprestimo:
    print('seu emprestimo foi NEGADO!')
else:
    print('Seu emprestimo foi APROVADO!')
