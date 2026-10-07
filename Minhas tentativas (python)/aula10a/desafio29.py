vel = float(input('Velocidade do carro: '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'A multa vai custar R${multa:.2f}')

