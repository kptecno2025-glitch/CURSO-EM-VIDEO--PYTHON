n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))

if n1 > n2:
    print('O \033[33mprimeiro valor\033[m é maior que o \033[34msegundo\033[m')
elif n1 < n2:
    print('O \033[33msegundor\033[m valor é maior que o \033[34mprimeiro\033[m')
else:
    print('\033[33mNão existe\033[m valor maior, ambos são \033[34miguais\033[m')