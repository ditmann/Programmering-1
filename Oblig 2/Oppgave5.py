import random


#kast av 3 darts
def enRunde(navn):
    kast1 = random.randrange(0,60)
    kast2 = random.randrange(0,60)
    kast3 = random.randrange(0,60)
    print("""
          Første kast: %i
          Andre  kast: %i
          Tredie kast: %i

          %s fikk %i poeng
          """ % (kast1,kast2,kast3,navn,kast1+kast2+kast3))
    

#starter runden hvis man får feil input starter den på nytt B)
def start():
    try:
        runde = 0
        spillere = int(input("hvor mange spillere er dere?"))
        while runde < spillere:
            enRunde(input("hva heter den som spiller?"))
            runde = runde+1
    except:
        print("her bruker vi titalls systemet .;,,,;.")
        start()


#kaller på start for å starte
start()