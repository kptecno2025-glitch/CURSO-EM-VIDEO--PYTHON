'''import random
al1 = input('primeiro aluno ')
al2 = input('segundo aluno ')
al3 = input('terceiro aluno ')
al4 = input('quarto aluno ')
lista = [al1, al2, al3, al4]

sorteado = random.shuffle(lista)

print('A ordem de apresentação será:')
print(lista)'''

from random import shuffle
al1 = input('primeiro aluno ')
al2 = input('segundo aluno ')
al3 = input('terceiro aluno ')
al4 = input('quarto aluno ')
lista = [al1, al2, al3, al4]
escolhido = shuffle(lista)

print('a ordem é:')
print(lista)
