n = int(input('Digite um numero inteiro: '))

print('Escolha a base de conversão: ')
print('1 - Binario')
print('2 - Octal')
print('3 - Hexadecimal')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{n} em binario é {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} em octal é {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} em hexadecimal é {hex(n)[2:]}')
else:
    print('\033[31mINVALIDO!')