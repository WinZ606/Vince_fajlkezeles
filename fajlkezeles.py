import random

def lista_letrehozas():
    i = 0
    szamok = []
    while i < 101:
        randomszam:int = int(random.random()*201)-50
        szamok.append(randomszam)
        i += 1
    return szamok

def lista_string(lista):
    szoveg:str = ""
    for i in range(0,len(lista),1):
        if (i<len(lista)-1):
            szoveg += f"{lista[i]}; "
        else:
            szoveg += f"{lista[i]}"
    return szoveg

def fajlba_mentes(szoveg):
    fajlom = open("adatok.txt", "w", encoding='utf-8')
    fajlom.write(szoveg)
    fajlom.close()

def fajlbol_olvas():
    fajlom = open("adatok.txt", "r", encoding='utf-8')
    szoveg = str(fajlom.read())
    lista = szoveg.split(";")
    lista2 = []
    for i in range(0, len(lista), 1):
        szam:int = int(lista[i].strip())
        lista2.append(szam)
    print(lista2)
    fajlom.close()