km = float(input('Distancia percorrida (km): '))
preço = km * 0.5
longa = km * 0.45
if km <= 200:
    print(f'O valor da viagem custou R${preço:.2f}')
else:
    print(f'O valor da viagem custou R${longa:.2f}')
