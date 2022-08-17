#Escreva um algoritmo que lê a idade de uma pessoa em anos e retorna a faixa
#etária em que ela se encontra com base na seguinte regra:
#a. Primeira Faixa: 0 – 18 anos;
#b. Segunda Faixa: 19 – 23 anos;
#c. Terceira Faixa: 24 – 28 anos;
#d. Quarta Faixa: 29 – 33 anos;
#e. Quinta Faixa: Acima de 33 anos.


idade = int(input("Qual a sua idade?"))
while idade < 0:
    idade = int(input("Qual a sua idade? (Defina valores positivos)"))


if idade >= 0 and idade <= 18:
    print("Você faz parte da Primeira Faixa.")
elif idade > 18 and idade <= 23:
    print("Você faz parte da Segunda Faixa.")
elif idade > 23 and idade <= 28:
    print("Você faz parte da Terceira Faixa.")
elif idade > 28 and idade <= 33:
    print("Você faz parte da Quarta Faixa.")
else:
    print("Você faz parte da Quinta Faixa.")
