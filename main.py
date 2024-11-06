import fajlkezeles
import feladatok

lista = fajlkezeles.lista_letrehozas()
szoveg = fajlkezeles.lista_string(lista)
fajlkezeles.fajlba_mentes(szoveg)
fajlkezeles.fajlbol_olvas()
print("\nfeladatok: ")
print(f"Ennyi negatív szám van: {feladatok.feladat1(lista)}")
print(f"Ez a legnagyobb szám: {feladatok.feladat2(lista)}")
print(f"Páros elemek: {feladatok.feladat3(lista)}")
print(f"Ennyi az öttel osztható elemek összege: {feladatok.feladat4(lista)}")
print(f"A lista legkisebb eleme a {feladatok.feladat5(lista)}. helyen áll")