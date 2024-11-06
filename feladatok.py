import fajlkezeles

def feladat1(lista):
    i = 0
    negativdb = 0
    while i < len(lista):
        if lista[i] < 0:
            negativdb += 1
        i += 1
    return negativdb

def feladat2(lista):
    i = 0
    max_index:int = 0
    while i < len(lista):
        if (lista[i] > lista[max_index]):
            max_index = i
        i += 1
    return lista[max_index]

def feladat3(lista):
    i = 0
    paros = []
    while i < len(lista):
        if lista[i] % 2 == 0:
            paros.append(lista[i])
        i += 1
    return paros

def feladat4(lista):
    i = 0
    otosok = 0
    while i < len(lista):
        if lista[i] % 5 == 0:
            otosok += lista[i]
        i += 1
    return otosok

def feladat5(lista):
    i = 0
    min_index:int = 0
    while i < len(lista):
        if (lista[i] < lista[min_index]):
            min_index = i
        i += 1
    return min_index