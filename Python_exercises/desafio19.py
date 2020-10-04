import random
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
Lista = [n1, n2, n3]
r = random.choice(Lista)
print('O nome escolhido foi {}!'.format(r))