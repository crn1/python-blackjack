import math
import time
import random
from pocetna import *
from sto import *

class Igra:

    def __init__(self, novac, tezina):
        self.novac = novac
        self.tezina = tezina
        self.krug = 0
        self.minUlog = 0
        self.rezultat = 0
        
    def postaviMinUlog(self):
        if self.tezina == 1:
            self.minUlog += (self.novac // 20)
        elif self.tezina == 2:
            self.minUlog += (self.novac // 15)
        else:
            self.minUlog += (self.novac // 10)

    def noviKrug(self):
        self.krug += 1
        iznosKarata = 0

        clear()
        self.postaviMinUlog()

        if self.novac < self.minUlog:
            self.rezultat += self.krug*self.rezultat//10 
            self.rezultat *= (self.tezina + (self.tezina / 10))

            print("\n Iznos Vašeg novca je manji od minimalnog uloga za ovaj krug i zato igra više ne\n može da se nastavi.\n\n\t\t\t* * * UKUPAN REZULTAT: {0} * * *\n ".format(math.floor(self.rezultat)))  
            input(" Pritisnite ENTER za povratak na početnu stranicu.")

        else:
            self.prikaziStatistiku()

            self.ulog = -1
            while self.ulog < self.minUlog or self.ulog > self.novac:
                self.ulog = int(input("\n Unesite ulog za ovaj krug: "))
                if self.ulog < self.minUlog or self.ulog > self.novac:
                    print("\n Vaš ulog mora biti veći od minimalnog uloga za ovaj krug, a manji ili jednak\n iznosu novca koji posedujete.")

            mojSto = Sto()
            mojSto.dodajKartu()
            mojSto.dodajKartu()
            self.prikaziSto(mojSto)

    def prikaziSto(self, mojSto):
        clear()
        self.prikaziStatistiku()
        
        mojSto.prikazi() #"\n\n Ukupan iznos Vaših karata je: {0}".format(mojSto.vrednost))

        if mojSto.vrednost > 21:
            print("\n IZGUBILI ste ulog za ovaj krug jer Vam vrednost karata prelazi 21.\n")
            input(" Pritisnite ENTER za ulazak u sledeći krug.")
            self.novac -= self.ulog

            self.noviKrug()

        else:
            odgovor = input("\n Da li želite da vučete još jednu kartu (d/n)? ").upper()

        if odgovor == "D":
            mojSto.dodajKartu()
            self.prikaziSto(mojSto)
        else:
            self.uporedjivanje(mojSto)

    def uporedjivanje(self, mojSto):
        clear()
        self.prikaziStatistiku()
        mojSto.prikazi()

        print("\n\n\t\t\t* * * Delilac igra * * *")
        time.sleep(random.randint(3, 7))

        protivnickiSto = Sto()
        protivnickiSto.dodajKartu()
        protivnickiSto.dodajKartu()

        if self.tezina == 1:
            while protivnickiSto.vrednost < 15:
                protivnickiSto.dodajKartu()
        elif self.tezina == 2:
            while protivnickiSto.vrednost < 16:
                protivnickiSto.dodajKartu()
        elif self.tezina == 3:
            while protivnickiSto.vrednost < mojSto.vrednost:
                protivnickiSto.dodajKartu()

        protivnickiSto.prikazi()
        time.sleep(3)
        print("\n\n Ukupan iznos protivničkih karata je: {0}".format(protivnickiSto.vrednost))


        if mojSto.vrednost > protivnickiSto.vrednost:
            self.pobeda("POBEDILI ste u ovom krugu jer imate veću vrednost karata od delioca.")
        elif protivnickiSto.vrednost > 21:
            self.pobeda("POBEDILI ste u ovom krugu jer protivnik ima vrednost karata preko 21.")
        elif mojSto.vrednost == protivnickiSto.vrednost:
            if len(mojSto.karte) < len(protivnickiSto.karte):
                self.pobeda("POBEDILI ste u ovom krugu jer ste izvukli manje karata od delioca.")
            if len(mojSto.karte) > len(protivnickiSto.karte):
                self.poraz("IZGUBILI ste u ovom krugu jer je delilac izvukao manji broj karata.") 
            if len(mojSto.karte) == len(protivnickiSto.karte):
                self.nereseno() 
        elif mojSto.vrednost < protivnickiSto.vrednost:
            self.poraz("IZGUBILI ste u ovom krugu jer imate manju vrednost karata od delioca!")

        input("\n Pritisnite ENTER za početak sledećeg kruga.")
        self.noviKrug()

    def pobeda(self, razlog):
        dobitak = 0

        if self.tezina == 1:
            dobitak = self.ulog * 2 
        elif self.tezina == 2:
            dobitak = self.ulog * 1.5
        elif self.tezina == 3:
            dobitak = self.ulog

        print("\n", razlog, "\n Dobitak bez uloga za ovaj krug iznosi: {0}".format(dobitak))
        self.novac += dobitak
        self.rezultat += dobitak

    def nereseno(self):
        print("\n Ovaj krug je NEREŠEN jer Vi i delilac imate istu vrednost i broj karata.\n Vraćen Vam je ulog.")
        
    def poraz(self, razlog):
        print("\n", razlog, "\n Izgubili ste Vaš ulog za ovaj krug.")
        self.novac -= self.ulog

    def prikaziStatistiku(self):
        print("\n===============================================================================\n\tKrug broj: {0}\t|\tNovac: {1}\t|\tMinimalni ulog: {2}\n===============================================================================".format(self.krug, self.novac, self.minUlog)) 



