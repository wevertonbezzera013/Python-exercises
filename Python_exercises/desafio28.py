import random
print('='*40)
print(' '* 5, 'JOGO DE ADIVINHAÇÃO!')
print('='*40)
num = int(input('Digite um número de 0 a 5: '))
a = random.choice([0,5])
print('='*10, 'PROCESSANDO', '='*17)
if num == a:
    print('Você acertou! Eu pensei no número {}!'.format(a))
else:
    print('Você errou! Eu pensei no número {}!'.format(a))
print('='*40)