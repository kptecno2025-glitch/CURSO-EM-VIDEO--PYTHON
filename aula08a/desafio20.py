import random

al1 = input('digite o nome do aluno: ')
al2 = input('digite o nome do aluno: ')
al3 = input('digite o nome do aluno: ')
al4 = input('digite o nome do aluno: ')

lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('a ordem de apresentação será: ')
print(lista)

