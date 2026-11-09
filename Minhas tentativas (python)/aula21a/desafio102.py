def fatorial(n, show=False):

    '''-->Calcula o Fatorial de um numero.
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um numero n.'''


    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')
    return f

print('-'*30)
print(fatorial(5, show=True))

print('-'*30)
print(fatorial(5))

print('-'*30)
help(fatorial)


