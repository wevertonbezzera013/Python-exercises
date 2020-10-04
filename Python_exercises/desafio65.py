resp = 'S'
cont = som = med = maior = menor = 0

while resp == 'S':
    num = int(input('Digite um número: '))
    som += num
    cont += 1
    
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    resp = str(input('Quer continuar?[S/N] ')).strip().upper()

print('Você digitou {} números.'.format(cont))
print('A soma dos números é igual a {}.'.format(som))
med = som / cont
print('A média dos números é igual a {}.'.format(med))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
