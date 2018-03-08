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

            plista = ("Pukosi jbg", "PUKOSI BRT", ":'(", "eeee moj ti pukosi", "zuriosm", "jesi", "da", "Pukosi. Ignorisem.", "PUKOSIDER", "pa pa pa pa pa paranoja", "smrk", "mrk", "popusio si jbg", "ASI TUNJAV PA NEMOZES TAKO IGRATI", "zec", "LUUUUUUUUUUUUUUKA", "e ovaj si se poslednji potez zajebao.... pukosi", "propo", "propo ko muda kroz suplje gace", "asi grindzav sta?")
            print("\n {0}\n\n\t\t\t* * * UKUPAN REZ: {1} * * *\n ".format(random.choice(plista), math.floor(self.rezultat)))  
            input(" Pritisnider ENTER za povratak na početnu stranicu.")

        else:
            self.prikaziStatistiku()

            self.ulog = -1
            while self.ulog < self.minUlog or self.ulog > self.novac:
                self.ulog = int(input("\n Unesider ulog za ovaj krug: "))
                if self.ulog < self.minUlog or self.ulog > self.novac:
                    lista = ["Esi ti kreten?", "Ozb si debil lepo kucaj", "Nemere to ludi"]
                    print("\t\t\t  ", radnom.choice(lista))

            mojSto = Sto()
            mojSto.dodajKartu()
            mojSto.dodajKartu()

            while True: 
                clear()
                self.prikaziStatistiku()
                mojSto.prikazi() #"\n\n Ukupan iznos Vaših karata je: {0}".format(mojSto.vrednost))

                if mojSto.vrednost > 21:
                    print("\n PRESHO 21 AHHHAHAHAHAHAHAHAHAHHAHAHAHAHA :'(\n")
                    input(" Pritisnider ENTER za ulazak u sledeći krug.")
                    self.novac -= self.ulog
                    break

                else:
                    odgovor = input("\n Oćeš vući još jednu kartu (SAMO ĆU REĆI D/n? ").upper()

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
            self.pobeda("Pobedio si. Ignorišem.")
        elif protivnickiSto.vrednost > 21:
            self.pobeda("Pobedio si. Čestitam.")
        elif mojSto.vrednost == protivnickiSto.vrednost:
            if len(mojSto.karte) < len(protivnickiSto.karte):
                self.pobeda("Pobedio si brt. Hvala.")
            if len(mojSto.karte) > len(protivnickiSto.karte):
                self.poraz("Izgubio si zato sto da.") 
            if len(mojSto.karte) == len(protivnickiSto.karte):
                self.nereseno() 
        elif mojSto.vrednost < protivnickiSto.vrednost:
            self.poraz("Izgubio si. Sto si prso?")

        input("\n Pritisnider ENTER za početak sledećeg kruga.")

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
        print("\n Ovaj krug je NEREŠEN. ok")
        
    def poraz(self, razlog):
        print("\n", razlog, "\n Izgubili ste Vaš ulog za ovaj krug.")
        self.novac -= self.ulog

    def prikaziStatistiku(self):
        temp = ""
        if self.tezina == 3:
            if self.novac > 1000:
                temp = " (ok.)"
            elif self.novac > 2000:
                temp = " (usercina mrtva)"
            elif self.novac > 3000:
                temp = " (JEBENI BOLE)"
            elif self.novac > 5000:
                temp = " (SISTEMA)"
        else:
            if self.novac == 200:
                temp = " :)"

        print("===============================================================================\n\tKrug: {0}\t\t|\tIQ: {1}{2}\t|\tMinimalni ulog: {3}\n===============================================================================".format(self.krug, self.novac, temp, self.minUlog)) 
