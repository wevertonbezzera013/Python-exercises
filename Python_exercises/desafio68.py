from random import randint

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? ')).strip().upper()
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}.')
    
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
    
    
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')

    print('Vamos jogar novamente...')
print(f'Game Over. Você venceu {v} vezes!')