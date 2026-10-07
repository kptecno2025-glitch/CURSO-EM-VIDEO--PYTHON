n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}') #"[2:] é pra fatear string, ou seja, a string ira pular os dois primeiros digitos
elif opção == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif opção == 3:
    print(f'convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção invalida! Tente novamente.')

