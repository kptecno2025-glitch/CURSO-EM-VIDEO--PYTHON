distancia = int(input('Qual é a distancia da sua viagem? '))
if distancia <= 200:
    preço = distancia * 0.5
else:
    preço = distancia * 0.45
print(f'O preço da sua viagem custa \033[32mR${preço:.2f}')
