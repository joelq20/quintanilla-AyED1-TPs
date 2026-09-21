#sander quintanilla 

#Escribir funciones para:
#a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
#a través del teclado.
#b. Recibir una lista como parámetro y devolver True si la misma contiene algún
#elemento repetido. La función no debe modificar la lista.
#c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
#únicos de la lista original, sin importar el orden.
#Combinar estas tres funciones en un mismo programa

import random as r


# a. generaro una lista de N numeros random 
def generar_lista(n):
    lista = []

    for i in range(n):
        lista.append(r.randint(1, 100))

    return lista


# b. este verifica si hay elementos repetidos
def tiene_repetidos(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True

    return False


# c. este otro crea una lista con los elementos únicos
def elementos_unicos(lista):
    nueva_lista = []

    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)

    return nueva_lista


#LUGAR PRINCIPAL

n = int(input("Ingrese la cantidad de números: "))

while n < 0:
    print("La cantidad no puede ser negativa.")
    n = int(input("Ingrese la cantidad de números: "))

lista = generar_lista(n)

print("Lista original:")
print(lista)

if tiene_repetidos(lista):
    print("La lista tiene elementos repetidos.")
else:
    print("La lista no tiene elementos repetidos.")

lista_unica = elementos_unicos(lista)

print("Lista con elementos únicos:")
print(lista_unica)