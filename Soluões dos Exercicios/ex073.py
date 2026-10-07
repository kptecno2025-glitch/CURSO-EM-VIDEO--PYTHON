brasileirão = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR',
               'Bragatino', 'Bahia', 'Coritiba', 'São Paulo', 'Atlético Mineiro',
               'Corithians', 'Cuzeiro', 'Bota Fogo', 'Vitória', 'Internacional',
               'Santos', 'Grêmio', 'Vasco', 'Remo', 'Mirasol', 'Chapecoense')
print('-='*20)
print(f'Lista de times {brasileirão}')
print('-='*20)

print(f'Os 5 primeiros colocados são {brasileirão[0:5]}')
print('-='*20)

print(f'Os 4 ultimos colocados são {brasileirão[-4:]}')
print('-='*20)

print(f'Times em ordem alfabetica {sorted(brasileirão)}')
print('-='*20)

print(f'O Chapecoense está na {brasileirão.index('Chapecoense')+1} posição')