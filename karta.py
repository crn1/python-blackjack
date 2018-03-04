import random

class Karta:

    znakovi = ("PIK", "KARO", "TREF", "SRCE", "CUMUR")
    imena = ("JEDINICA", "DVOJKA", "TROJKA", "ČETVORKA", "PETICA", "ŠESTICA", "SEDMICA", "OSMICA", "DEVETKA", "DESETKA", "ŽANDAR", "DAMA", "KRALJ") 

    def __init__(self):
        self.znak = random.randint(1, 4)
        self.ime = random.randint(0, 12)
        self.stringZnak = self.znakovi[self.znak] 
        self.stringIme = self.imena[self.znak] 
        self.postaviCharIme()
        self.postaviCharZnak()
        self.odrediVrednost()

    def odrediVrednost(self):
        if self.ime >= 9:
            self.vrednost = 10
        elif self.ime == 0:
            self.vrednost = "j"
        else:
            self.vrednost = self.ime + 1 

    def postaviCharIme(self):
        if self.ime == 0:
            self.charIme = "A"
        elif self.ime == 10:
            self.charIme = "J"
        elif self.ime == 11:
            self.charIme = "Q"
        elif self.ime == 12:
            self.charIme = "K"
        else:
            self.charIme = self.ime + 1

    def postaviCharZnak(self):
        if self.znak == 0:
            self.charZnak = "♠"
        elif self.znak == 1:
            self.charZnak = "♦"
        elif self.znak == 2:
            self.charZnak = "♣"
        elif self.znak == 3:
            self.charZnak = "♥"
        elif self.znak == 4:
            self.charZnak = "•" 
