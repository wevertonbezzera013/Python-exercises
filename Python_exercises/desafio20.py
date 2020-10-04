import random
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
Lista = [n1, n2, n3]
random.shuffle(Lista)
print('A ordem escolhida foi:')
print(Lista)