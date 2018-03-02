from pocetna import *

class Igra:

    def __init__(self, novac, tezina):
        self.novac = novac
        self.tezina = tezina
        self.krug = 1
        self.min_ulog = 0
        
    def postavi_min_ulog(self):
        if self.tezina == 1:
            self.minimalni_ulog += (self.novac / 30)
        elif self.tezina == 2:
            self.minimalni_ulog += (self.novac / 20)
        elif self.tezina == 3:
            self.minimalni_ulog += (self.novac / 10)

    def novi_krug(self):
        clear()
        self.postavi_min_ulog()
        self.prikazi_statistiku()

    def prikazi_statistiku(self):
        print("\tKrug broj: {0}\t|\tNovac: {1}\t|\tMinimalni ulog: {2}\n===============================================================================".format(self.krug, self.novac, self.min_ulog)) 


