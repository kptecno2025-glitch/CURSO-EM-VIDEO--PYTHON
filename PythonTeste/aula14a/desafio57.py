sexo = input('Digite seu sexo: [M/F] ').upper()

while sexo != 'M' and sexo != 'F':
    print('Sexo invalido, tente novamente')
    sexo = input('Digite seu sexo: [M/F] ').upper()

print('Sexo registrado com sucesso')
