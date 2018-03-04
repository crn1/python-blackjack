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

    def prikazi(self):
        prikaz = []
        for x in range(0, 5):    
            prikaz.append("")
            for karta in self.karte:

                prikaz[x] += "\t"

                if x == 0 or x == 4:
                    prikaz[x] += "-------"
                elif x == 1:
                    if len(str(karta.charIme)) == 2:
                        prikaz[x] += "|{0}{1}  |".format(karta.charIme, karta.charZnak)
                    else:
                        prikaz[x] += "|{0}{1}   |".format(karta.charIme, karta.charZnak)
                elif x == 2:
                        prikaz[x] += "|     |"
                elif x == 3:
                    if len(str(karta.charIme)) == 2:
                        prikaz[x] += "|  {0}{1}|".format(karta.charIme, karta.charZnak)
                    else:
                        prikaz[x] += "|   {0}{1}|".format(karta.charIme, karta.charZnak)

                if len(self.karte) <= 5:
                    prikaz[x] += "\t"

        prikaz_formiran = "\n".join(prikaz)
        print("\n", prikaz_formiran) 
            
