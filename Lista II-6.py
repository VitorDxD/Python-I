#Os usuários de um plano de saúde tiveram seus planos reajustados com base na
#sua faixa etária (As faixas são as mesmas da questão 5). Escreva um algoritmo
#que lê a idade do usuário e o valor da sua mensalidade e calcula o valor do
#reajuste, sabendo que o percentual de reajuste obedece a seguinte regra:
#a. Primeira Faixa: 6.5%
#b. Segunda Faixa: 7.75%
#c. Terceira Faixa: 8.2%
#d. Quarta Faixa: 8.5%
#e. Quinta Faixa: 9%

idade = int(input("Qual a sua idade?"))
while idade < 0:
    idade = int(input("Qual a sua idade? (Defina valores positivos)"))

if idade >= 0 and idade <= 18:
    porc = 6.5/100
elif idade > 18 and idade <= 23:
    porc = 7.75/100
elif idade > 23 and idade <= 28:
    porc = 8.2/100
elif idade > 28 and idade <= 33:
    porc = 8.5/100
else:
    porc = 9/100

plano = int(input("Qual o valor da mensalidade?"))
print ("O valor do reajuste é de R$", plano * porc)

