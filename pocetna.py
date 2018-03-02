import os
from igra import *

clear = lambda: os.system("clear")
novac, tezina = None, None

def pocetna_stranica():
    stranica = """
                        PYTHON BLACK-JACK ĐORĐA GLUVAJIĆA                               
                                     V.0.0.1
                                
                                
                        Pritisnite ENTER za nastavak . . .
    """
    clear()
    print(stranica)
    input("")
    izaberi_tezinu()

def izaberi_tezinu():
    stranica = """
                        PYTHON BLACK-JACK ĐORĐA GLUVAJIĆA                               
                                     V.0.0.1
                                
                                
                               Izaberite težinu igre:

                                1. Normalno
                                2. Teško
                                3. Nemoguće
    """
    clear()
    print(stranica)
    global tezina
    tezina = input("")
    igra = Igra(1000, tezina)
    igra.novi_krug()

if __name__ == "__main__":
    pocetna_stranica()

