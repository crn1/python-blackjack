import os
from igra import *

clear = lambda: os.system("clear")

def pocetna_stranica():
    stranica = """
                      .===================================.
                      | PYTHON BLACK-JACK ĐORĐA GLUVAJIĆA |                              
                      |              V0.0.1               | 
                      .===================================.
                                
                                
                                   1. Normalno
                                   2. Teško
                                   3. Nemoguće
    """
    clear()
    print(stranica)
    tezina = -1
    while tezina < 1 or tezina > 3:
        tezina = int(input("\t\t\tIzaberite težinu igre (1/2/3): "))
        if tezina < 1 or tezina > 3:
            print("\n\tUnesite brojeve '1', '2' ili '3' da biste izabrali težinu igre.\n")

    igra = Igra(50, tezina)
    igra.noviKrug()

    pocetna_stranica()

if __name__ == "__main__":
    pocetna_stranica()

