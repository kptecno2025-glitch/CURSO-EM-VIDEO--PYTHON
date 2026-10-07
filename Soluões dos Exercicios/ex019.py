'''import random
al1 = input('primeiro aluno ')
al2 = input('segundo aluno ')
al3 = input('terceiro aluno ')
al4 = input('quarto aluno ')

lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))'''

from random import choice
al1 = input('primeiro aluno ')
al2 = input('segundo aluno ')
al3 = input('terceiro aluno ')
al4 = input('quarto aluno ')
lista = [al1, al2, al3, al4]
escolhido = choice(lista)
print(f'o aluno escolhido foi {escolhido}')
