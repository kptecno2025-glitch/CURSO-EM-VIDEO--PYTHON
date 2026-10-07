from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0

while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')

    opção = int(input('>>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado entre {n1} X {n2} é igual a {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opção == 4:
        print('Informe novos numeros')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, Tente novamente')
    print('-=' * 10)
    sleep(2)
print('Fim do programa, Volte sempre!')
