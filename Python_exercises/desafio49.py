print('×='*15)
print('    T A B U A D A')
print('×='*15)

for c in range(1):
    n = int(input('Digite um número: '))
    for d in range(0, 10):
        print('{} × {} = {}'.format(d, n, d*n))
print('Fim!')