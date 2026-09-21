#Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
#donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valo-
#res de la lista

lista = []

n = int(input("Ingrese hasta que numero desea calcular los cuadrados: "))


for i in range(1, n + 1):
    lista.append(i ** 2)

print("Lista:", lista)
print()
print("Últimos 10 valores:", lista[-10:]) 
# al ser -10 va al principio del final de la lista ademas de que los pide la consigna 