#sander quintanilla 

#Desarrollar una función que reciba como parámetros dos números enteros positivos
#y devuelva como valor de retorno el número que resulte de concatenar ambos
#parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se per-
#mite utilizar facilidades de Python no vistas en clase

def concatenado(a,b):
    resultado = str(a) + str(b)
    return int(resultado)

a = int(input("Ingrese la primera serie o numero entero positivo: "))
b = int(input("Ingrese la segunda serie o numero entero positivo: "))

print(concatenado(a, b))