#Escribir una función que reciba una lista de números enteros como parámetro y la
#normalice, es decir que todos sus elementos deben sumar 1.0, respetando las pro-
#porciones relativas que cada elemento tiene en la lista original. Desarrollar también
#un programa que permita verificar el comportamiento de la función. Por ejemplo,
#normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50]

lista = [ 1 , 1 , 2 , 4 ]

def normalizar(lista):
    suma = sum(lista)
    # Divide cada elemento por la suma total para que la lista sume 1
    for i in range(len ( lista)):
        lista[i] = lista[i] / suma

    return lista

print("Lista normalizada:", normalizar(lista))