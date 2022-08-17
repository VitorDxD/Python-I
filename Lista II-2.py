#O valor de um carro novo é composto pela soma do seu Custo de Fabricação,
#Margem do Distribuidor e Impostos. Sabendo que a Margem do Distribuidor é
#de 19% e que os impostos são 40%, ambos calculados com base no Custo de
#Fabricação. Escreva um algoritmo que lê o Custo de Fabricação e nos retorna
#qual o valor final do carro;

custoFabr = int(input("Qual o custo de fabricação do carro?"))
MargDistr = (19/100) * custoFabr
Impostos = (40/100) * custoFabr

ValorCarro = custoFabr + MargDistr + Impostos
print("O valor final do carro é R$", ValorCarro)

