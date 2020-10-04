num = soma = cont = 0
num = int(input('Digite um número [digite 999 para parar]: '))

while num != 999:
     soma += num
     cont += 1
     num = int(input('Digite um número [digite 999 para parar]: '))

print('Você digitou {} números.'.format(cont))
print('A soma dos números é igual a {}.'.format(soma))