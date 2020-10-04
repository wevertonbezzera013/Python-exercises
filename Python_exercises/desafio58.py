from random import randint

print('''Olá! sou seu computador!
	Acabei de pensar em um número entre 0 e 10!
	Será que você consegue adivinhar qual foi?''')
	
computador = randint(0, 10)
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    
    if jogador == computador:
        acertou = True
        
    else:
        if jogador < computador:
            print('O número que eu pensei é maior que esse!')
        elif jogador > computador:
            print('O número que eu pensei é menor que esse.')
        
print('Acertou com {} palpites!'.format(palpite))
        
