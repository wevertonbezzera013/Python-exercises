produto = float(input('Qual é o preço do produto? '))
desconto = produto - (produto * 5/100)
print('Seu produto no valor de R$ {} com desconto de 5%, passa a valer R$ {}'.format(produto, desconto))