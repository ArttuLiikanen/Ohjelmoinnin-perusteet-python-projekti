class Esine:
    hinta = 0
    nimi = ""

    def __init__(self, hinta, nimi, skin):
        self.hinta = hinta
        self.nimi = nimi
        self.skin = skin
        

class Tili:
    saldo = 0

    def __init__(self, saldo):
        self.saldo = saldo

    def Talletus(self, talletus):
        self.saldo += talletus

    def Nosto(self, nostoMaara):
        self.saldo -= nostoMaara

    def NaytaSaldo(self):
        print("Tililläsi on nyt", self.saldo, "euroa rahaa")
