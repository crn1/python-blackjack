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

        clear()
        self.postaviMinUlog()

        if self.novac < self.minUlog:
            self.rezultat += self.krug*self.rezultat//10
            self.rezultat *= (self.tezina + (self.tezina / 10))

            print("\n Izgubili ste sav novac, time gubeći i ovu igru!\n\n\t\t\t* * * UKUPAN REZULTAT: {0} * * *\n ".format(int(self.rezultat)))
            input(" Pritisnite ENTER za povratak na početnu stranicu.")

        else:
            self.prikaziStatistiku()

            self.ulog = -1
            while self.ulog < self.minUlog or self.ulog > self.novac:
                self.ulog = int(input("\n Unesite ulog za ovaj krug: "))
                if self.ulog < self.minUlog or self.ulog > self.novac:
                    print(" Vaš ulog mora ne sme da bude manji od minimalnog uloga za ovaj krug i iznosa\n Vašeg novca!")

            mojSto = Sto()
            mojSto.dodajKartu()
            mojSto.dodajKartu()

            while True:
                clear()
                self.prikaziStatistiku()
                mojSto.prikazi() #"\n\n Ukupan iznos Vaših karata je: {0}".format(mojSto.vrednost))

                if mojSto.vrednost > 21:
                    print("\n Iznos vaših karata prelazi 21. Izgubili ste Vaš ulog za ovaj krug.")
                    input(" Pritisnite ENTER za ulazak u sledeći krug.")
                    self.novac -= self.ulog
                    break

                else:
                    odgovor = input("\n Da li hoćete da vučete još jednu kartu (d/n)? ").upper()

                if odgovor == "D":
                    mojSto.dodajKartu()

                else:
                    self.uporedjivanje(mojSto)
                    break

            self.noviKrug()

    def uporedjivanje(self, mojSto):
        clear()
        self.prikaziStatistiku()
        mojSto.prikazi()

        print("\n\n\t\t\t* * * Domaćin igra * * *")
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
            self.pobeda("Iznos Vaših karata je veći od domaćinovog. POBEDILI ste u ovom krugu!")
        elif protivnickiSto.vrednost > 21:
            self.pobeda("Domaćinov iznos karata prelazi 21. POBEDILI ste u ovom krugu!")
        elif mojSto.vrednost == protivnickiSto.vrednost:
            if len(mojSto.karte) < len(protivnickiSto.karte):
                self.pobeda("Iako imate iste iznose karata, POBEDILI ste jer ste vukli manje karata.")
            if len(mojSto.karte) > len(protivnickiSto.karte):
                self.poraz("Iako imate iste iznose karata, IZGUBULI ste jer je domaćin vukao manje karata.")
            if len(mojSto.karte) == len(protivnickiSto.karte):
                self.nereseno()
        elif mojSto.vrednost < protivnickiSto.vrednost:
            self.poraz("Iznos Vaših karata je manji od domaćinovog. IZGUBILI ste u ovom krugu!")

        input("\n Pritisnite ENTER za početak sledećeg kruga.")

    def pobeda(self, razlog):
        dobitak = 0

        if self.tezina == 1:
            dobitak = self.ulog * 2
        elif self.tezina == 2:
            dobitak = math.floor(self.ulog * 1.5)
        elif self.tezina == 3:
            dobitak = self.ulog

        print("\n", razlog, "\n Dobitak bez uloga za ovaj krug iznosi: {0}".format(dobitak))
        self.novac += dobitak
        self.rezultat += dobitak

    def nereseno(self):
        print("\n Ovaj krug je NEREŠEN!")

    def poraz(self, razlog):
        print("\n", razlog, "\n Izgubili ste Vaš ulog za ovaj krug.")
        self.novac -= self.ulog

    def prikaziStatistiku(self):
        print("===============================================================================\n\tKrug: {0}\t\t|\tNovac: {1}\t|\tMinimalni ulog: {2}\n===============================================================================".format(self.krug, self.novac, self.minUlog))
