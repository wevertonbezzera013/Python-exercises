p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(t), end='')
        t += r
        cont += 1
    print('Pausa!')
    mais = int(input('Quantos termos você quer a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))