def leiaInt(msg):
    while True:
        dado = str(input(msg))
        if dado.isnumeric() == True:
            dado = int(dado)
            break
        else:
            print(f'\033[0:31mERRO! Digite um numero inteiro válido.\033[m ')
    return dado





# Programa principal
n = leiaInt(('Digite um numero: '))
print(f'Você acabou de digitar o numero {n}')
