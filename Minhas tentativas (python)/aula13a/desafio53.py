frase = str(input('Digite uma frase: '))

    #Remove espaços e deixa tudo minusculo
frase_limpa = frase.replace(' ', ' ').lower()

    #inverte a frase
invertida = frase_limpa[::-1]
print(invertida)

if frase_limpa == invertida:
    print('É um palindromo')
else:
    print('Não é um palindromo')
