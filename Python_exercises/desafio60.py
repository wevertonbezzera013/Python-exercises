n = int(input('Digite um número \npara calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' × ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('{}.'.format(f))
