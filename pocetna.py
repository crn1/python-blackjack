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
                      .==M=A=N=Dž=U=R=I=J=A=N==E=D=I=Š=N==.
                                
                                     Ja sam: 
                            ========================
                            1. Malo mudo
                            2. Veliko mudo
                            3. Sistemaš

                            0. Debil (izađi napolje)
    """
    clear()
    print(stranica)
    tezina = -1

    while tezina < 0 or tezina > 3:
        tezina = int(input("\t\t\tIzaberder opciju (1/2/3/0): "))
        if tezina < 0 or tezina > 3:
            lista = ("Esi ti kreten?", "Ozb si debil lepo kucaj", "Nemere to ludi")
            print("\t\t\t  ", radnom.choice(lista))

    if tezina >= 1 and tezina <= 3:
        igra = Igra(50, tezina)
        igra.noviKrug()
        pocetna_stranica()

    elif tezina == 0:
        sys.exit()

if __name__ == "__main__":
    pocetna_stranica()

