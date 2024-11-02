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

cardBack = top_l_corner + hor_line + hor_line + hor_line + hor_line + top_r_corner + "\n" + vert_line + kløver + "  " + hjerte + vert_line + "\n" + vert_line + ruter + "  "+spar + vert_line + "\n" + bot_l_corner + hor_line + hor_line + hor_line + hor_line + bot_r_corner
print(cardBack)

#lister for å holde litt kontroll
slagAvKort = [hjerte,spar,kløver,ruter]
typeKort=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

        

#laer kortstokken
class Cards:
          
    def __init__(self,):
        self.cards = []
        self.points = 0


    def nykortstokk(self):
        self.kort = []
        for slag in slagAvKort:
            for typer in typeKort:
                self.kort.append(slag + typer)


    def shuffle(self):
        rng.shuffle(self.kort)


    def draw(self):
        self.cards.append(deck.kort[0])
        del deck.kort[0]
        


    def getPoints(self):
        self.points = 0
        ace = 0
        for cards in self.cards:
            if cards[-1] == "2":
                self.points += 2
            elif cards [-1] == "3":
                self.points += 3
            elif cards [-1] == "4":
                self.points += 4
            elif cards [-1] == "5":
                self.points += 5
            elif cards [-1] == "6":
                self.points += 6
            elif cards [-1] == "7":
                self.points += 7
            elif cards [-1] == "8":
                self.points += 8
            elif cards [-1] == "9":
                self.points += 9
            elif cards [-1] == "A":
                self.points += 11
                ace += 1
            elif cards [-1] == "10" or "J" or "Q" or "K":
                self.points += 10

        while self.points > 21 and ace > 0:
            self.points -= 10
            ace -= 1

        return self.points

def begin():
    player.draw()
    dealer.draw()
    player.draw()
    dealer.draw()

#def paintCard(cardList):
#    for card in cardList:
#        type = card[0]
#        number = card[-1]
#        painting = top_l_corner + hor_line + hor_line + hor_line + hor_line + top_r_corner + "\n" + vert_line + number+"  "+ type + vert_line + "\n" + vert_line + type + "  "+number+ vert_line + "\n" + bot_l_corner + hor_line + hor_line + hor_line + hor_line + bot_r_corner
#        return painting
#def table():
#    print(f"""
#Dealer:
#{paintCard(dealer.cards)}
#{cardBack}""")





#spillet   
gaming = True     
deck = Cards()
deck.nykortstokk()
deck.shuffle()
dealer = Cards()
player = Cards()
begin()

#while gaming == True:





