# Sander Quintanilla
#Desarrollar una función que reciba tres números enteros positivos y devuelva el
#mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
#caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
#también un programa para ingresar los tres valores, invocar a la función y mostrar
#el máximo hallado, o un mensaje informativo si éste no existe.

def mayor_unico(a, b, c):
    if a > b:
        if a > c:
            return a
    if b > a: 
        if b > c:
            return b
    if c > a:
        if c > b:
            return c
    return -1


a=int(input("Ingrese el primer número entero positivo: "))
b=int(input("Ingrese el segundo número entero positivo: "))
c=int(input("Ingrese el tercer número entero positivo: "))

if mayor_unico(a, b, c) != -1:
    print("El mayor número único es:", mayor_unico(a, b, c))
else:
    print("No hay un mayor número único.")

