# sander quintanilla

#Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
#para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
#cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
#caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
#de alguna naranja se encuentra fuera del rango indicado se la clasifica para
#procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
#cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
#jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
#reparto. Simular el peso de cada unidad generando un número entero al azar entre
#150 y 350.
#Además, se desea saber cuántos camiones se necesitan para transportar la cose-
#cha, considerando que la ocupación del camión no debe ser inferior al 80%; en
#caso contrario el camión no serán despachado por su alto costo


import random as r
r.seed(1)


def generar_naranjas(cantidad):# controlador de  naranjas!

    naranjas = []

    for i in range(cantidad):
        peso = r.randint(150, 350)
        naranjas.append(peso)

    return naranjas


def clasificar_naranjas(naranjas):
    aptas = []
    jugo = 0

    for peso in naranjas:# funciona como filtro de cuales son apropiadas 
        if peso >= 200 and peso <= 300:
            aptas.append(peso)
        else:
            jugo += 1

    return aptas, jugo


def calcular_cajones(aptas): # ahce la correcta division de naranjas en cajones
    cajones = len(aptas) // 100
    sobrantes = len(aptas) % 100

    return cajones, sobrantes


def calcular_camiones(aptas, cajones):
    camiones = 0
    peso_camion = 0

    for i in range(cajones):
        peso_cajon = sum(aptas[i * 100:(i + 1) * 100])

        if peso_camion + peso_cajon <= 500000:
            peso_camion += peso_cajon

        else:
            if peso_camion >= 400000:
                camiones += 1

            peso_camion = peso_cajon

    if peso_camion >= 400000:
        camiones += 1

    return camiones

cantidad = int(input("Ingrese la cantidad de naranjas cosechadas: "))

naranjas = generar_naranjas(cantidad)

aptas, jugo = clasificar_naranjas(naranjas)

cajones, sobrantes = calcular_cajones(aptas)

camiones = calcular_camiones(aptas, cajones)

print("Cajones completos:", cajones)
print("Naranjas para jugo:", jugo)
print("Naranjas sobrantes:", sobrantes)
print("Camiones necesarios:", camiones)