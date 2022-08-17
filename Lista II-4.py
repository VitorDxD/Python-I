#Escreva um algoritmo que lê a idade de uma pessoa separada por anos, meses e
#dias e retorna a idade da pessoa em dias. Para esse exemplo, considere um mês
#comercial com 30 dias.

anos = int(input("Quantos anos você tem?"))
meses = int(input("Quantos meses?"))
dias = int(input("E quantos dias?"))

vidaDias = (anos*12*30) + (meses*30) + dias
print("Você tem", vidaDias, "dias de vida.")
