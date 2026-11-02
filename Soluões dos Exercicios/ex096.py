def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m2')

# Programa principal
print('Controle de Terrenos')
print('-'*30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l,c)
