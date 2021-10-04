import circle as c

class Zwembad:

    binnen_cirkel:c.Circle = c.Circle(2)
    buiten_cirkel:c.Circle = c.Circle(3)

    def __init__(self, straal_zwembad, breedte_pad):
        self.binnen_cirkel = c.Circle(straal_zwembad)
        self.buiten_cirkel = c.Circle(breedte_pad + straal_zwembad)

    def prijs_omheining(self):
        return self.buiten_cirkel.omtrek() * 20

    def prijs_pad(self):
        opp = self.buiten_cirkel.oppervlakte() - self.binnen_cirkel.oppervlakte()
        return opp * 35

    def totaal(self):
        return self.prijs_pad() + self.prijs_omheining()
