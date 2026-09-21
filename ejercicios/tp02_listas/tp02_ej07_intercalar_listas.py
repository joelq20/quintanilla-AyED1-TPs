#Intercalar los elementos de una lista entre los elementos de otra. La intercalación
#deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
#una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
#y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
#tener distintas longitudes.


def intercalar(lista1,lista2):
    for i in range(len(lista2)):

         # esta calculara la posición donde se insertará cada elemento
        posicion = i * 2 + 1
        lista1[posicion:posicion] = [lista2[i]]

lista1 = [8, 1, 3]
lista2 = [5, 9, 7]

intercalar(lista1, lista2)
print(lista1)
