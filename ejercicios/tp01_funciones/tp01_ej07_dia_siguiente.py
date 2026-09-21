# sander quintanilla

#Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
#fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
#correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
#ni agregados, desarrollar programas que permitan:

#a. Sumar N días a una fecha.
#b. Calcular la cantidad de días existentes entre dos fechas cualesquiera

dias = [31,28,31,30,31,30,31,31,30,31,30,31]
# vuelve a aplicar en parte lo de fechas validad del ejercicio 2
def diasiguiente(dia,mes,anio):

    if anio % 400 == 0:
        dias [1] = 29 
    elif anio % 100 != 0 and anio % 4 == 0:
        dias [1] = 29

    dia += 1

    if dia > dias [mes - 1 ]:
        dia = 1 
        mes += 1

    if mes > 12:
        mes = 1 
        anio += 1

    return dia , mes , anio



opcion = 0

while opcion != 3:

    print("\n 1. Sumar Numeros de días a una fecha")
    print("2. Calcular días entre dos fechas")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:

        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        año = int(input("Ingrese el año: "))

        n = int(input("Ingrese la cantidad de dias que quieras sumar al actual!: "))

        for i in range(n):
            dia, mes, año = diasiguiente(dia, mes, año)

        print("La fecha resultante es:", dia, "/", mes, "/", año, "😸")

    elif opcion == 2:

        dia1 = int(input("Ingrese el día de la primera fecha: "))
        mes1 = int(input("Ingrese el mes de la primera fecha: "))
        año1 = int(input("Ingrese el año de la primera fecha: "))

        dia2 = int(input("Ingrese el día de la segunda fecha: "))
        mes2 = int(input("Ingrese el mes de la segunda fecha: "))
        año2 = int(input("Ingrese el año de la segunda fecha: "))

        cantidad = 0

        while dia1 != dia2 or mes1 != mes2 or año1 != año2:

            dia1, mes1, año1 = diasiguiente(dia1, mes1, año1)

            cantidad += 1

        print("La cantidad de días entre las fechas es:", cantidad, "😸")

    elif opcion == 3:
        print("Programa finalizado.")

    else:
        print("Opción inválida.")