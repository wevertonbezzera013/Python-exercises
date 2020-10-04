#for c in range(1, 7): #vai escrever de 1 até 6, pq o último ele ignora
    #print(c)
#print('FIM!')

#for c in range(6, 0, -1): #vai escrever de trás pra frente
    #print(c)
#print('FIM!')

#n = int(input('Digite um número: '))
#for c in range(0, n+1):
    #print(c)
#print('Fim!')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim!')