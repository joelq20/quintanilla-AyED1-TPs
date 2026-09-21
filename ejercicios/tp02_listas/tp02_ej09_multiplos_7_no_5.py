#Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
#ue no sean múltiplos de 5. A y B se ingresar desde el teclado

#comparte relacion con la anterior por ende tambien es compacta!

a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))

while a > b:
	print("A debe ser menor o igual que B.")
	a = int(input("Ingrese el valor de A: "))
	b = int(input("Ingrese el valor de B: "))

# Guarda los numeros divisibles por 7 que no sean divisibles por 5.
lista = [i for i in range(a,b + 1) if i % 7 == 0 and i % 5 != 0]

print(lista)