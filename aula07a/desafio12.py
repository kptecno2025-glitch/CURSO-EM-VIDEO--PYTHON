preço = (input('digite o preço do produto: '))
preço = preço.replace('R$', '').replace(',', '.')
preço = float(preço)
desconto = preço * 0.05
novo_preço = preço - desconto
print(f'preço original: R${preço:.2f}')
print(f'desconto (5%): R${desconto:.2f}')
print(f'novo preço: R${novo_preço:.2f}')

