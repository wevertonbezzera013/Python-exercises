dis = float(input('Qual a distância da sua viagem? '))
p1 = dis * 0.50
p2 = dis * 0.50
if dis <= 200:
    print('Sua viagem sem desconto custará R${:.2f}!!'.format(p1))
else:
    print('Sua viagem com desconto custará R${:.2f}!!'.format(p2))