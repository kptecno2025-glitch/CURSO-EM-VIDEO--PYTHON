from time import sleep
def contador(inicio, fim, passo):
    cont = inicio
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio < fim:
        print('-=' * 30)
        print('Contagem de 1 até 10 de 1 em 1')
        while cont <= fim:
            print(f'{cont} ', end='')
            cont+= passo
            sleep(1)
        print('FIM!', end='')
        print()
        print('-=' * 30)
    elif inicio > fim:
        print('Contagem de 10 até 0 de 2 em 2')
        while cont >= fim:
            print(f'{cont} ',end='')
            cont -= passo
            sleep(1)
        print('FIM!', end='')
        print()
        print('-=' * 30)

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
