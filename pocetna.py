import os
import sys
import random
from igra import *

clear = lambda: os.system("clear")

def pocetna_stranica():
    stranica = """
                      .===================================.
                      | PYTHON BLACK-JACK ĐORĐA GLUVAJIĆA |
                      |              V0.0.1               |
                      .===================================.

                                Izaberite težinu:
                            ========================
                            1. Normalno
                            2. Teško
                            3. Nemoguće

                            0. Izađi iz aplikacije
    """
    clear()
    print(stranica)
    tezina = -1

    while tezina < 0 or tezina > 3:
        tezina = int(input("\t\t\tIzaberte opciju (1/2/3/0): "))
        if tezina < 0 or tezina > 3:
            print("\t\t\t\t\t\t Uneli ste pogrešnu vrednost")

    if tezina >= 1 and tezina <= 3:
        igra = Igra(50, tezina)
        igra.noviKrug()
        pocetna_stranica()

    elif tezina == 0:
        sys.exit()

if __name__ == "__main__":
    pocetna_stranica()

