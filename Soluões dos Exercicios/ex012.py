preço = float(input('qual o preço do produto? R$'))
desconto = preço * 0.05
novo_preço = preço - desconto
print('o produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo_preço))

