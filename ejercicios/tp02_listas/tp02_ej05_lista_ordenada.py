#Escribir una función que reciba una lista como parámetro y devuelva True si la lista
#está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
#ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
#además un programa para verificar el comportamiento de la función

lista = [ 10 , 20 , 30 ]

def ordenada(lista):
    for i in range(len(lista) -1):
        if lista[i] > lista [i + 1]:
            return False 
    return True

print("lista",lista)
print("estaba ordenada?", ordenada(lista))