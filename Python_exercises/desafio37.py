print('Digite 1 para converter para BINÁRIO.')
print('Digite 2 para converter para OCTAL.')
print('Digite 3 para converter para HEXADECIMAL.')
num = int(input('Digite um número: '))
con = int(input('Escolha uma operação: '))
if con == 1:
    print('O número {} convertido para BINÁRIO é {}.'.format(num, bin(num[2:])))
elif con == 2:
    print('O número {} convertido para OCTAL é {}.'.format(num, oct(num[2:])))
elif con == 3:
    print('O número {} convertido para HEXADECIMAL é {}.'.format(num, hex(num[2:])))
else:
    print('Obrigado e volte sempre.')