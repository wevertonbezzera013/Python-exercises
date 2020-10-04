n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
if n1 > n2:
    print('{} é MAIOR que {}!!'.format(n1, n2))
elif n1 < n2:
    print('{} é MENOR que {}!!'.format(n1, n2))
elif n1 == n2:
    print('Os valores são os mesmos.')
else:
    print('Obrigado e volte sempre.')