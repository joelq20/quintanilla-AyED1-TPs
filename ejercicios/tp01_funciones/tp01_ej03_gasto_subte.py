#Sander 

#Una persona desea llevar el control de los gastos realizados al viajar en el subte-
#rráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un es-
#quema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarro-
#llar una función que reciba como parámetro la cantidad de viajes realizados en un
#determinado mes y devuelva el total gastado en viajes. Realizar también un pro-
#grama para verificar el comportamiento de la función

#Viajes	y precios por viaje para visualizar y verificar que este bien
#1–20	$1.753
#21–30  $1.402,40
#31–40  $1.227,10
#41+    $1.051,80

def viaje_subte(viajes):
    tarifa = 1753

    if viajes <= 20: 
        descuento = 0 

    elif viajes <= 30:
        descuento = 0.20

    elif viajes <= 40:
        descuento = 0.30
    else:
        descuento = 0.40

    final = tarifa - tarifa * descuento

    return viajes * final

viajes = int(input("Ingrese la cantidad de viajes realizados en el mes: "))
print("El total gastado en el mes es: $", viaje_subte(viajes))