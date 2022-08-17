#Escreva um algoritmo que lê as duas notas de um aluno e calcula a média
#ponderada dessas notas, sabendo que a primeira nota tem peso 4 e a segunda
#nota peso 6;

nota1 = int(input("Qual foi a primeira nota?"))
nota2 = int(input("Qual foi a segunda nota?"))
mediaP = (nota1*4 + nota2*6) / 10

print ("A média ponderada foi", mediaP, "(Nota 1 = Peso 4 | Nota 2 = Peso 6)")
