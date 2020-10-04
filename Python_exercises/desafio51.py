a1 = int(input('Digite o primeiro termo: '))
n = int(input('Digite o número de termos: '))
r = int(input('Digite a razão: '))
an = 0
for c in range(a1, n, r):
    an = a1 + (n - 1) * r
    
print('o enésimo termo é {}!'.format(an))
print('Fim!')