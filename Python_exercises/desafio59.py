print(' ')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

print(' ')
print('/''=/'*14)
print('             O P E R A Ç Ã O')
print('/''=/'*14)
print(' ')

opção = 0

while opção != 5:
    print('''    Digite [1] para somar
    Digite [2] para multiplicar
    Digite [3] para o maior valor
    Digite [4] para novos números
    Digite [5] para sair do programa''')
    
    print(' ')
    opção = int(input('Digite a operação que deseja realizar: '))
    print(' ')
    print('/''=/'*14)
    print(' ')
    
    if opção == 1:
        print('A soma de {} e {} é igual a {}.'.format(n1, n2, n1+n2))
        print(' ')
    elif opção == 2:
        print('{} multiplicado por {} é igual a {}.'.format(n1, n2, n1*n2))
        print(' ')
    elif opção == 3:
        if n1 > n2:
            print('O maior valor é {}.'.format(n1))
            print(' ')
        else:
            print('O maior valor é {}.'.formar(n2))
            print(' ')
    elif opção == 4:
        print(' ')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        
print('Fim do programa, volte sempre!')