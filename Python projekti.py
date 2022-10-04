from math import inf
from random import randrange
from PythonProjektiLuokat import Esine
from PythonProjektiLuokat import Tili

def AvaaLaatikko(laatikkoHinta):
    if minunTili.saldo >= laatikkoHinta:
        print("\nLaatikon avaus maksaa", laatikkoHinta, "euroa. tahdotko varmasti avata laatikon?\n1: kyllä\n2: ei")
        valinta = TarkistaValinta(2)
        if valinta == 1:
            minunTili.Nosto(laatikkoHinta)
            esine = LaatikonGenerointi()
            inventaario.append(esine)
            print("\nSait esineen", esine.nimi, ",", esine.skin, "(arvo", esine.hinta, "euroa)")
        elif valinta == 2:
            return

    elif len(inventaario) == 0:
        print("\nSinulla ei näköjään ole tarpeeksi rahaa eikä esineitä myytäväksi. Ehkä vain tämän kerran annan sinun lisätä tilillesi haluamasi määrän.")
        rahanVaarennos = TarkistaValinta(inf)
        minunTili.Talletus(rahanVaarennos)
        minunTili.NaytaSaldo()
    else:
        print("\nSinulla ei ole tarpeeksi rahaa laatikon avaamiseen, mutta voit myydä aikaisempia saamiasia aseita saadaksesi lisää.")


def LaatikonGenerointi():
    numero = randrange(100)
    kerroin = randrange(50, 150)/100
    if numero in range(0, 13):
        esine = meteorite
    elif numero in range(13, 26):
        esine = atheris
    elif numero in range(26, 37):
        esine = memento
    elif numero in range(37, 47):
        esine = justice
    elif numero in range(47, 57):
        esine = codeRed
    elif numero in range(57, 66):
        esine = redLine
    elif numero in range(66, 74):
        esine = bulldozer
    elif numero in range(74, 82):
        esine = printstream
    elif numero in range(82, 88):
        esine = containmentBreach
    elif numero in range(88, 93):
        esine = handCannon
    elif numero in range(93, 97):
        esine = scorched
    elif numero in range(97, 100):
        esine = autotronic

    return esine


def MyyEsine():
    if len(inventaario) == 0:
        TarkasteleInventaariota()
    else:
        print("\nMinkä esineen haluat myydä?\n0 : Peruuta")
        EsineLista()
        valinta = TarkistaValinta(len(inventaario))
        if valinta == 0:
            return
        else:
            valittuEsine = inventaario[valinta-1]
            esineenNumero = inventaario.index(valittuEsine)
            print("\nHaluatko varmasti myydä esineen", valittuEsine.nimi, ",", valittuEsine.skin, ". Tilillesi lisätään", valittuEsine.hinta, "euroa.\n1: kyllä\n2: ei")
            valinta = TarkistaValinta(2)
            if valinta == 1:
                myyntiHinta = valittuEsine.hinta
                minunTili.Talletus(myyntiHinta)
                inventaario.pop(esineenNumero)
                minunTili.NaytaSaldo()
            elif valinta == 2:
                return


def TarkasteleInventaariota():
    if len(inventaario) == 0:
        print("\nInventaariosi on tyhjä!\nVoit täyttää sitä avaamalla laatikoita.")
    else:
        print("\nTässä inventaariosi:")
        EsineLista()
        

def EsineLista():
    for i in range(len(inventaario)):
        esine = inventaario[i]
        print(i+1, ":", esine.nimi, ",", esine.skin, "(", esine.hinta, "euroa )")


def TarkistaValinta(valintaMaara):
    valinta = input()
    while True:
        if valinta.isnumeric() == True and int(valinta) <= valintaMaara: 
            return int(valinta)
        else:
            valinta = input("Antamasi merkki ei ollut numero tai se on liian suuri tai pieni. Anna jokin yllä mainituista luvuista")


meteorite = Esine(2, "Desert eagle", "Meteorite") 
atheris = Esine(3, "AWP", "Atheris")
memento = Esine(3, "MAG-7", "Memento")
justice = Esine(9, "MAG-7", "Justice")
codeRed = Esine(29, "Desert eagle", "Code red")
redLine = Esine(50, "AWP", "Red line")
bulldozer = Esine(70, "MAG-7", "Bulldozer")
printstream = Esine(90, "Desert eagle", "Printstream")
containmentBreach = Esine(150, "AWP", "Containment breach")
handCannon = Esine(450, "Desert eagle", "Hand cannon")
scorched = Esine(500, "Karambit", "Scorched")
autotronic = Esine(1400, "Karambit", "Autotronic")

minunTili = Tili(50)
laatikkoHinta = 10
valinta = 0
inventaario = []

print("\nTervetuloa Counter Strike case simulaattoriin!")

while True:
    print("\nMitä haluaisit tehdä?\n1: Avaa laatikko\n2: Myy esine\n3: Tarkastele inventaariotasi")
    valinta = TarkistaValinta(3)
    if valinta == 1:
        AvaaLaatikko(laatikkoHinta)
    elif valinta == 2:
        MyyEsine()
    elif valinta == 3:   
        TarkasteleInventaariota()
        minunTili.NaytaSaldo()