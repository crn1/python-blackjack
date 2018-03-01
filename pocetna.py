import os

clear = lambda: os.system("clear")

def main():
    pocetna = """
                        PYTHON BLACK-JACK ĐORĐA GLUVAJIĆA                               
                                     V.0.0.1
                                
                                
                        Pritisnite ENTER za nastavak . . .
    """
    clear()
    print(pocetna)
    input("")
    
if __name__ == "__main__":
    main()

