# Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
#elementos de la primera que sean impares. El proceso deberá realizarse utilizando
#la función filter(). Imprimir las dos listas por pantalla


import random as r
r.seed(1)
lista = []

cantidad  = int(input("Ingrese la cantidad de números: "))

while cantidad < 0:
    print("La cantidad no puede ser negativa.")
    cantidad = int(input("Ingrese la cantidad de números: "))

for i in range(cantidad):
    lista.append(r.randint(1, 100)) #entonces

lista_nopar = list(filter(lambda x: x % 2 != 0 , lista))

print("Lista original:", lista)
print()
print("Lista con cositas impares:", lista_nopar)
