def area(larg, comp):
    tam = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {tam}m²')

larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)
