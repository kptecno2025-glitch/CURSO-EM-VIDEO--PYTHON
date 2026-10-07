a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

termo = a1
pa = 1

while pa <= 10:
    print(termo, end=' ')
    termo += r
    pa += 1
print()
mais = int(input('Mais termo: '))

while mais != 0:
    contador = 1
    while contador <= mais:
        contador += 1
        print(termo, end=' ')
        termo += r
    print()
    mais = int(input('Mais termo: '))
print('Fim')