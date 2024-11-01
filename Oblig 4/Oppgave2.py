import random as rng

#symboler
hjerte = "\u2665"
kløver = "\u2663"
ruter = "\u2666"
spar = "\u2660"
hor_line = '\u2500'
vert_line = '\u2502'
bot_l_corner = '\u2514'
top_l_corner = '\u250C'
bot_r_corner = '\u2518'
top_r_corner = '\u2510'
number = "5"

card = top_l_corner + hor_line + hor_line + hor_line + hor_line + top_r_corner + "\n" + vert_line + "5  " + hjerte + vert_line + "\n" + vert_line + hjerte + "  5" + vert_line + "\n" + bot_l_corner + hor_line + hor_line + hor_line + hor_line + bot_r_corner
print(card)

#lister for å holde litt kontroll
verdiPåKort = [2,3,4,5,6,7,8,9,10,10,10,11]
slagAvKort = [hjerte,spar,kløver,ruter]
typeKort=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
player = []
dealer = []
        

#laer kortstokken
class Kortstokk:
          
          def __init__(self):
             self.kortstokk = []

             for slag in slagAvKort:
                  for typer in typeKort:
                       self.kortstokk.append(slag + typer)
                       
                       
          def stokk(deck):
              rng.shuffle(deck.kortstokk)          
        
class Hands:
     def __init__(self):
          self.cards = []
            

deck = Kortstokk()

print(deck.kortstokk)
deck.stokk()

print(deck.kortstokk)
