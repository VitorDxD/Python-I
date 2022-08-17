#Escreva um algoritmo que lê a duração de uma atividade física em segundos e
#retorna o tempo em Horas : Minutos : Segundos;

duracao = int(input("Quanto tempo durou a atividade física? (Em segundos)"))

h = 00
min = 00
s = duracao

while s >= 60:
    s -= 60
    min += 1
while min >= 60:
    min -= 60
    h += 1


print(f"A atividade durou {h}:{min}:{s}")
