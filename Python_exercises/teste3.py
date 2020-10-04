from math import sqrt
#from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz do número {} é {}.'.format(num, math.ceil(raiz)))
print('A raiz do número {} é {}.'.format(num, math.floor(raiz))
print('A raiz do número {} é {:.2f}.'.format(num, raiz))