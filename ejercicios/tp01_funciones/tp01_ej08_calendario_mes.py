#sander quintanilla

#La siguiente función permite averiguar el día de la semana para una fecha determi-
#nada. La fecha se suministra en forma de tres parámetros enteros y la función de-
#vuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para
#imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
#y año cualquiera basándose en la función suministrada. Considerar que la semana
#omienza en domingo


def diadelasemana(dia, mes, anio):

    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2

    siglo = anio // 100
    anio2 = anio % 100

    diasem = (((26 * mes - 2) // 10) + dia + anio2 +
              (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7

    if diasem < 0:
        diasem = diasem + 7

    return diasem


mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

while mes < 1 or mes > 12:
    print("El mes debe estar entre 1 y 12.")
    mes = int(input("Ingrese el mes: "))

while anio < 1:
    print("El año debe ser positivo.")
    anio = int(input("Ingrese el año: "))

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if anio % 400 == 0 or (anio % 100 != 0 and anio % 4 == 0):
    dias[1] = 29

inicio = diadelasemana(1, mes, anio)
cantidad = dias[mes - 1]

print("DOM LUN MAR MIE JUE VIE SAB")

for i in range(inicio):
    print("    ", end="")

for dia in range(1, cantidad + 1):
    print(f"{dia:3}", end="")

    if (inicio + dia) % 7 == 0:
        print()