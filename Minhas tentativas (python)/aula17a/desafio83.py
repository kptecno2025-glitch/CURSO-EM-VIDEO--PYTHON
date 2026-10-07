pilha = []
usuario = str(input('Digite uma Expressão: '))
for pos in range(len(usuario)):
    if usuario[pos] == '(':
        pilha.append('(')
    elif usuario[pos] == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) > 0:
    print('Sua expressão está invalida')
else:
    print('Sua Expressão está valida')



