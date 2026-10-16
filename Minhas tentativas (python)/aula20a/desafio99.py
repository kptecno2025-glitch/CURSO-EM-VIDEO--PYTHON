from time import sleep
def maior(* num):
    tam = len(num)
    print('-=' * 30)
    print('Analisando os valores passados...')

    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
    print(f'Foram informados {tam} valores ao todo.')

    if tam > 0:
        maior_valor = max(num)
    else:
        maior_valor = 0
    print(f'O maior valor informado foi {maior_valor}')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
maior()