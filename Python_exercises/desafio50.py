s=0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um valor: {}'.format(c)))
    if num % 2 == 0:
      s += num
      cont = cont + 1
print('Você informou {} números PARES e a soma foi {}!'.format(num, s))
print('Fim!')