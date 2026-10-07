n = cont = s = 0
print('Digite 999 para encerrar')
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos {cont} valores foi {s}')