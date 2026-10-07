r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo')

    if r1 == r2 == r3:
        print('Triângulo equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')

else:
    print('Não é possível formar um triângulo')
