listagem = ('Sapato', 650,'Shampoo', 75.90,'Camiseta', 120,'Caneta', 25.50,'Bolsa', 462.75,'Ventilador', 819.99,'Controle-Remoto', 57,'Headphone', 790.60,'Iphone-17', 12999.99, 'Urna Funeraria', 2500.50,'Corda', 40.50,'Pilhas', 130.75,)
print('_'*40)
print('LISTAGEM DE PREÇOS-(BARATO)'.center(40))
print('_'*40)
for cont in range(0, len(listagem)):
    if cont % 2 == 0:
        print(f'{listagem[cont]:.<30}', end = ' ')
    else:
        print(f'R${listagem[cont]:>10.2f}')



