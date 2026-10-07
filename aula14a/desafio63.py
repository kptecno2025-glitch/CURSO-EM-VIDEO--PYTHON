n = int(input('Quantos termos deseja mostrar: '))

a = 0
b = 1
contador = 0

while contador < n:
    print(a, end=' -> ')

    a, b = b, a + b

    contador += 1
