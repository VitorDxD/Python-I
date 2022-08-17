#Um hotel cobra R$ 60.00 a diária e mais uma taxa de serviços. A taxa de
#serviços é de:
#a. R$5.50 por diária, se o número de diárias for maior que 15;
#b. R$6.00 por diária, se o número de diárias for igual a 15;
#c. R$8.00 por diária, se o número de diárias for menor que 15.
#Escreva um algoritmo que leia o número de diárias mostre o total da conta de
#um cliente.

diarias = int(input("Quantas diárias no hotel?"))

if diarias >= 0 and diarias < 15:
    taxaSer = 8
elif diarias == 15:
    taxaSer = 6
elif diarias > 15:
    taxaSer = 5.5
else:
    print("Valor inválido!")

print("Total da conta: R$", 60*diarias + taxaSer*diarias)


