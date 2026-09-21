#Eliminar de una lista de números enteros aquellos valores que se encuentren en
#una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
#resultante. La función debe modificar la lista original sin crear una copia modificada


lista = [10, 25, 30, 45, 50, 60, 75]
eliminar = [25, 50, 75]

def eliminar_valores(lista, eliminar):
    i = 0

    while i < len(lista):
        if lista[i] in eliminar:
            lista.pop(i)
        else:
            i += 1

print("Lista original:")
print(lista)
print()

print("Valores a eliminar:")
print(eliminar)
print()

eliminar_valores(lista, eliminar)

print("Lista resultante:")
print(lista)