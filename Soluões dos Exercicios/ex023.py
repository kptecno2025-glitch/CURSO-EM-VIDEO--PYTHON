num = int(input('Informe um numero: '))
#n = str(num)
print(f'Analisando o numero {num}')
'''print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')'''

print(f'Unidade: {num // 1 % 10}')
print(f'Dezenas: {num // 10 % 10}')
print(f'Centenas: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}')


