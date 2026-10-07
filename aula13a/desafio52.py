n = int(input('Digite um numero inteiro: '))
if n <= 1:
    print('Não é primo')
else:
    primo = True

    for c in range(2, n):
        if n % c == 0:
            primo = False
            break
    if primo:
        print('é primo')
    else:
        print('Não é primo')
