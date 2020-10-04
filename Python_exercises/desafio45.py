from random import randint

print('='*25)
print('PEDRA, PAPEL E TESOURA!')
print('='*25)

itens = ('PEDRA', 'PAPEL', 'TESOURA')
escolha = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
resposta = int(input('Digite sua resposta: ')
print('Você escolheu {}!'.format(itens[escolha]))
print('O computador escolheu {}!'.format(itens[escolha]))

if escolha == 0: #COMPUTADOR ESCOLHEU PEDRA
    if jogador == 0:
        print('Empate!')
        
    elif jogador == 1:
        print('Você ganhou!')
        
    elif jogador == 2:
        print('Você perdeu!')
        
    else:
        print('Jogada inválida!')
        
elif escolha == 1: #COMPUTADOR ESCOLHEU PAPEL
    if jogador == 0:
        print('Você perdeu!')
        
    if jogador == 1:
        print('Empate!')
        
    if jogador == 2:
        print('Você ganhou!')
        
    else:
        print('Resposta inválida!')
    
elif escolha == 2: #COMPUTADOR ESCOLHEU TESOURA
    if jogador == 0:
        print('Você ganhou!')
        
    if jogador == 1:
        print('Você perdeu!')
        
    if jogador == 2:
        print('Empate!')
        
    else:
        print('Resposta inválida!')
    
