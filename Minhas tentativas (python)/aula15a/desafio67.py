n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} X {cont} = {n*cont}')
print('Programa Tabuada encerrada!')