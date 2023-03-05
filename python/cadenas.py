from itertools import combinations
import random

#print(random.randint(0,9))



def isUnique(lista, palabra): #funcion que define si la palabra es unica en todo el arreglo de cadenas
    for str in lista:
        if str == palabra:
            return False
    return True

def generaRandomString(tamanio):
    cadena = ''
    for i in range (0 ,tamanio):
        cadena = cadena + alfabeto[random.randint(0,1)]
    return cadena

def generaListaTamanio(tamanio):
    tamanioLista = 2**tamanio
    lista = []
    while len(lista) < tamanioLista:
        cadena = generaRandomString(tamanio)
        #print(cadena)
        if(isUnique(lista, cadena)):
            lista.append(cadena)
            #print(lista)
    return lista


def agregaTodo(listaFinal, lista):
    for str in lista:
        listaFinal.append(str)


def generaTodasListas(tamanio =1000):
    maxLen = tamanio
    listaFinal = []
    for i in range (2,(tamanio+1)):
        print("Current size: " + str(i))
        listaCadenas = generaListaTamanio(i)
        agregaTodo(listaFinal, listaCadenas)
    return listaFinal
    

alfabeto=['a','b']
lista = generaTodasListas()
print(lista)

