from karta import *

class Sto:

    def __init__(self):
        self.vrednost = 0
        self.karte = []

    def dodajKartu(self):
        temp_karta = Karta()
        self.karte.append(temp_karta)
        if temp_karta.vrednost == "j":
            if (self.vrednost + 11) > 21:
                self.vrednost += 1
            else:
                self.vrednost += 11
        else:
            self.vrednost += temp_karta.vrednost

    def izbrisiKarte(self):
        self.karte[:] = []

    def dobijStringKarata(self):
        prikaz = []
        for x in range(0, 5):    
            prikaz.append("")
            for karta in self.karte:
                if x == 0 or x == 4:
                    prikaz[x] += "\t-------\t"
                elif x == 1:
                    if len(str(karta.charIme)) == 2:
                        prikaz[x] += "\t|{0}{1}  |\t".format(karta.charIme, karta.charZnak)
                    else:
                        prikaz[x] += "\t|{0}{1}   |\t".format(karta.charIme, karta.charZnak)
                elif x == 2:
                    prikaz[x] += "\t|     |\t"
                elif x == 3:
                    if len(str(karta.charIme)) == 2:
                        prikaz[x] += "\t|  {0}{1}|\t".format(karta.charIme, karta.charZnak)
                    else:
                        prikaz[x] += "\t|   {0}{1}|\t".format(karta.charIme, karta.charZnak)

        prikaz_formiran = "\n".join(prikaz)

        return prikaz_formiran
        
