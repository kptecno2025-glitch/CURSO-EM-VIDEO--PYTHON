n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
''')

    opcao = int(input('Sua opção: '))

    if opcao == 1:
        print(f'{n1} + {n2} = {n1 + n2}')

    elif opcao == 2:
        print(f'{n1} x {n2} = {n1 * n2}')

    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print('Os dois valores são iguais')

    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Saindo do programa...')

    else:
        print('Opção inválida! Tente novamente.')

print('Fim do programa')