nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Você foi aprovado.')
elif media < 5:
    print('Você foi reprovado.')
elif 7 > media >= 5:
    print('Você está em recuperação.')