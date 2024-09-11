
pakkeListe = []
#operasjoner man kan gjøre på lista

# legger til ting i lista
def leggTil(ting):
    pakkeListe.append(ting)
    loop()


#skriv ut lista under hverandre (lettere å lese)
def skrivUt():
    for ting in pakkeListe:
        print(ting)
    loop()

#fjerner ting fra lista
def fjern(ting):
    pakkeListe.remove(ting)
    loop()

#avslutter programmet
def slutt():
    for ting in pakkeListe:
        print(ting)
        

#loopen
def loop():
    print("""
                
          
          -Legge til ting skriv:        1
          -Fjerne ting skriv:           2
          -skrive ut lista skriv:       3
          -avslutte og få lista:        69
          """)
    try:
        valg = int(input())
        if valg == 1:
            leggTil(input("hva vil du legge til?\n"))
        elif valg == 2:
            fjern(input("hva vil du fjerne?\n"))
        elif valg == 3:
            skrivUt()
        elif valg == 69:
            slutt()
        else:
            print("det var ikke et av valgene (sinna fjes)")
    except:
        print("""
              
              
              
                    du må skrive ett av tallene
              
              
              
              
              """)
        loop()






print("\n\n\nnå skal vi lage pakkeliste!")
loop()