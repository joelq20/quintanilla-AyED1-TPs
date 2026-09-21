#Sander quintanilla 
#Desarrollar una función que reciba tres números enteros positivos correspondientes
#al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
#enerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
#Devolver True o False según la fecha sea correcta o no. Realizar también un
#programa para verificar el comportamiento de la función

def fecha_valida(dia, mes ,anio):

    if mes < 1 or mes > 12:
        return False

    bisiesto = False

    if anio % 400 == 0:
        bisiesto = True
    elif anio % 100 != 0:
        if anio % 4 == 0:
            bisiesto = True
    if mes == 2:
        if bisiesto:
            return dia <= 29
        else:
            return dia <= 28
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return dia <= 30
    if mes >= 1 and mes <= 12:
        return dia <= 31

    return False

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

if fecha_valida(dia, mes, anio):
    print("La fecha es válida.")
else: 
    print("la fecha no es valida.")