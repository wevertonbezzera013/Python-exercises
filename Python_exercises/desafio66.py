n = s = q = 0

while True:
    n = int(input('Digite um valor ou 999 para parar: '))
    if n == 999:
        break
    q += 1
    s += n
print(f'Você digitou {q} números.')
print(f'A soma desses valores é igual a {s}.')