    #USANDO WHILE
'''n = int(input('Digite um numero: '))

resultado = 1

while n > 1:
    resultado *= n
    n -= 1
print(resultado)'''

    #USANDO FOR
n = int(input('Digite um numero: '))
resultado = 1

for i in range(1, n+1):
    resultado *= i
print(resultado)