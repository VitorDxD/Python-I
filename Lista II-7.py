#Escreva um algoritmo que lê o diâmetro de uma circunferência e calcula a sua
#área. Sabemos que o diâmetro da circunferência é duas vezes o valor do raio e
#que a área de uma circunferência é calculada pela fórmula Área = π * Raio ^2
import math

diametro = int(input("Digite um valor para o diâmetro da circunferência:"))
raio = diametro / 2
area = math.pi * (raio ** 2)
print("A área da circunferência é {:.2f}".format (area))
