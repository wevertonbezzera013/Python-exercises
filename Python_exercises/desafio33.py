a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor digitado foi {}!!'.format(menor))
maior = b
if a>b and a>c:
    maior = a
if c>a and c>b:
    maior = c
print('O maior valor digitado foi {}!!'.format(maior))