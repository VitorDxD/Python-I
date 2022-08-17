#Escreva um algoritmo que lê o peso e a altura de uma pessoa e retorna seu
#Índice de Massa Corporal – IMC e sua classificação. Sabemos que IMC = Peso /
#Altura 2.
#a. Até 16,9 – Muito abaixo do peso;
#b. Entre 17 e 18,4 – Abaixo do peso;
#c. Entre 18,5 e 24,9 – Peso normal;
#d. Entre 25 e 29,9 – Acima do peso;
#e. Entre 30 e 34,9 – Obesidade grau I;
#f. Entre 35 e 40 - Obesidade grau II;
#g. Acima de 40 - Obesidade grau III.

peso = float(input("Qual seu peso? (Ex: 69.5) "))
altura = float(input("Qual sua altura? (Ex: 1.70) "))
IMC = peso / (altura ** 2)

if IMC < 17:
    IMCr = "Muito abaixo do peso"
elif IMC >= 17 and IMC < 18.5:
    IMCr = "Abaixo do peso"
elif IMC >= 18.5 and IMC < 25:
    IMCr = "Peso normal"
elif IMC >= 25 and IMC < 30:
    IMCr = "Acima do peso"
elif IMC >= 30 and IMC < 35:
    IMCr = "Obesidade grau I"
elif IMC >= 35 and IMC <= 40:
    IMCr = "Obesidade grau II"
else:
    IMCr = "Obesidade grau III"


print("Sua definição:", IMCr)
