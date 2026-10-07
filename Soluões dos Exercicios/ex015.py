dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
alug = dias * 60 + km * 0.15
print('O valor a pagar pelo aluguel é de R${:.2f}'.format(alug))
