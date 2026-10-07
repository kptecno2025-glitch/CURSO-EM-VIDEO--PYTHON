ano = float(input('Em que ano vc ta? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É ano \033[31mbissexto\033[m!')
else:
    print('Não é ano \033[34mbissexto\033[m!')


