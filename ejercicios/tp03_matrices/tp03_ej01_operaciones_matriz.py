#Desarrollar cada una de las siguientes funciones y escribir un programa que permi-
#ta verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada fun-
#ción:
#a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
#teclado.
#b. Ordenar en forma ascendente cada una de las filas de la matriz.
#c. Intercambiar dos filas, cuyos números se reciben como parámetro.
#d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
#e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
#f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
#parámetro.
#g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú-
#mero se recibe como parámetro.
#h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
#i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
#j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
#una lista con los números de las mismas.
#NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
#sea el valor ingresado



def cargar_matriz(n):
    matriz = []

    for i in range(n):
        fila = []

        for j in range(n):
            numero = int(input("Ingrese un número: "))
            fila.append(numero)

        matriz.append(fila)

    return matriz


def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


def ordenar_filas(matriz):
    for fila in matriz:
        fila.sort()


def intercambiar_filas(matriz, fila1, fila2):
    aux = matriz[fila1]
    matriz[fila1] = matriz[fila2]
    matriz[fila2] = aux


def intercambiar_columnas(matriz, columna1, columna2):
    for i in range(len(matriz)):
        aux = matriz[i][columna1]
        matriz[i][columna1] = matriz[i][columna2]
        matriz[i][columna2] = aux


def trasponer(matriz):
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux


def promedio_fila(matriz, fila):
    suma = 0

    for elemento in matriz[fila]:
        suma += elemento

    return suma / len(matriz[fila])


def porcentaje_impares_columna(matriz, columna):
    cantidad_impares = 0

    for i in range(len(matriz)):
        if matriz[i][columna] % 2 != 0:
            cantidad_impares += 1

    return cantidad_impares * 100 / len(matriz)


def es_simetrica_principal(matriz):
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False

    return True


def es_simetrica_secundaria(matriz):
    n = len(matriz)

    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[n - 1 - j][n - 1 - i]:
                return False

    return True


def columnas_capicua(matriz):
    columnas = []
    n = len(matriz)

    for j in range(n):
        capicua = True

        for i in range(n // 2):
            if matriz[i][j] != matriz[n - 1 - i][j]:
                capicua = False

        if capicua:
            columnas.append(j)

    return columnas


# Programa principal

n = int(input("Ingrese el tamaño de la matriz: "))

matriz = cargar_matriz(n)

print("\nMatriz original:")
mostrar_matriz(matriz)


# Ordenamos cada fila de la matriz
ordenar_filas(matriz)

print("\nMatriz con las filas ordenadas:")
mostrar_matriz(matriz)


# Intercambiamos dos filas elegidas por el usuario
fila1 = int(input("\nIngrese la primera fila a intercambiar (desde 0): "))
fila2 = int(input("Ingrese la segunda fila a intercambiar (desde 0): "))

intercambiar_filas(matriz, fila1, fila2)

print("\nMatriz después de intercambiar las filas:")
mostrar_matriz(matriz)


# Intercambiamos dos columnas elegidas por el usuario
columna1 = int(input("\nIngrese la primera columna a intercambiar (desde 0): "))
columna2 = int(input("Ingrese la segunda columna a intercambiar (desde 0): "))

intercambiar_columnas(matriz, columna1, columna2)

print("\nMatriz después de intercambiar las columnas:")
mostrar_matriz(matriz)


# Trasponemos la matriz sobre sí misma
trasponer(matriz)

print("\nMatriz traspuesta:")
mostrar_matriz(matriz)


# Calculamos el promedio de una fila
fila = int(input("\nIngrese una fila para calcular su promedio (desde 0): "))

print("Promedio de la fila:", promedio_fila(matriz, fila))


# Calculamos el porcentaje de impares de una columna
columna = int(input("\nIngrese una columna para calcular el porcentaje de impares (desde 0): "))

print("Porcentaje de impares:", porcentaje_impares_columna(matriz, columna), "%")


# Comprobamos la simetría respecto de la diagonal principal
if es_simetrica_principal(matriz):
    print("\nLa matriz es simétrica respecto de la diagonal principal.")
else:
    print("\nLa matriz no es simétrica respecto de la diagonal principal.")


# Comprobamos la simetría respecto de la diagonal secundaria
if es_simetrica_secundaria(matriz):
    print("La matriz es simétrica respecto de la diagonal secundaria.")
else:
    print("La matriz no es simétrica respecto de la diagonal secundaria.")


# Buscamos las columnas que son capicúa
columnas = columnas_capicua(matriz)

print("\nColumnas que son capicúa:", columnas)