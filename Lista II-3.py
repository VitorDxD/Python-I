#Sabendo que uma disciplina possui 40 aulas e que o percentual mínimo de
#presença é de 75%. Escreva um algoritmo que lê as duas notas do aluno e a sua
#quantidade de faltas e nos retorne o status do aluno com base na seguinte regra:
    #a. Caso a média aritmética das notas seja superior a 7 e a quantidade de
    #faltas for menor ou igual a 25% = APROVADO;
    #b. Caso a média aritmética das notas seja inferior a 7 e a quantidade de
    #faltas for menor ou igual a 25% = REPROVADO;
    #c. Caso a quantidade de faltas for superior a 25% = REPROVADO POR
    #FALTA;

nota1 = int(input("Qual sua primeira nota?"))
nota2 = int(input("Qual sua segunda nota?"))
faltas = int(input("Quantas aulas você faltou? (Max = 40)"))

media = nota2 + nota1 / 2
porcF = (faltas/40) * 100


while faltas > 40 or faltas < 0:
    faltas = int(input("Quantas aulas você faltou? (Max = 40)"))


if media >= 7 and porcF <= 25:
    print("Aprovado!")
elif media < 7 and porcF <= 25:
    print("Reprovado!")
else:
    print("Reprovado por falta!")
