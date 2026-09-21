# Sander Quintanilla

# Desarrollar cada una de las siguientes funciones y escribir un programa que per-
# mita verificar su funcionamiento imprimiendo la lista luego de invocar a cada fun-
# cion:
# a. Cargar una lista con numeros al azar de cuatro digitos. La cantidad de elemen-
# tos tambien sera un numero al azar de dos digitos.
# b. Calcular y devolver el producto de todos los elementos de la lista anterior.
# c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
# se ingresa desde el teclado y la funcion lo recibe como parametro. No utilizar
# listas auxiliares.
# d. Determinar si el contenido de una lista cualquiera es capicua, sin usar listas
# auxiliares. Un ejemplo de lista capicua es [50, 17, 91, 17, 50].

import random as r
r.seed(1)

# a. Cargar una lista con numeros al azar
def cargar_lista():
    cantidad = r.randint(10, 99)
    lista = []

    for i in range(cantidad):
        numero = r.randint(1000, 9999)
        lista.append(numero)

    return lista


# b. Calcular el producto de todos los elementos
def producto_lista(lista):
    producto = 1

    for numero in lista:
        producto = producto * numero

    return producto


# c. Eliminar todas las apariciones de un valor
def eliminar_valor(lista, valor):
    i = 0

    while i < len(lista):
        if lista[i] == valor:
            lista.pop(i)
        else:
            i += 1


# d. Determinar si una lista es capicúa :D
def es_capicua(lista):
    i = 0
    j = len(lista) - 1

    while i < j:
        if lista[i] != lista[j]:
            return False

        i += 1
        j -= 1

    return True


# Programa principal

lista = cargar_lista()

print("Lista original:")
print(lista)

producto = producto_lista(lista)
print("Producto de los elementos:", producto)

valor = int(input("Ingrese el valor que desea eliminar: "))

eliminar_valor(lista, valor)

print("Lista luego de eliminar el valor:")
print(lista)

print("¿La lista es capicúa?", es_capicua(lista))