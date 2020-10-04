n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
#print('A soma vale {}.'.format(n1 + n2))
s = n1 + n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
print('Soma {} \n Divisão {:.3f} \n Multiplicação {} \n Divisão Inteira {} \n Exponencial {} \n Resto {}'.format(s, d, m, di, e, r), end='====')