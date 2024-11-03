import random as rng
import time


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

#tester å tegne kort
#cardBack = top_l_corner + hor_line + hor_line + hor_line + hor_line + top_r_corner + "\n" + vert_line + kløver + "  " + hjerte + vert_line + "\n" + vert_line + ruter + "  "+spar + vert_line + "\n" + bot_l_corner + hor_line + hor_line + hor_line + hor_line + bot_r_corner
#print(cardBack)

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
    
    def botHitter(self):
        score = self.getPoints()
        print(f"dealer cards {dealer.cards} points: {score}\n")
        while score < 17:
            self.draw()
            time.sleep(1)
            print("HIT")
            score = self.getPoints()
            time.sleep(1)
            print(f"dealer cards: {self.cards} points: {self.getPoints()}\n")
    
    def playing(self):
        stand = False
        points = self.getPoints()
        while stand == False and points < 20 or stand == True and points > 20 :
            choise = (input("1-HIT or 2-Stand?\n"))
            if choise == "1":
                self.draw()
                points = self.getPoints()
                print(f"your cards: {self.cards} Points: {points}")

                time.sleep(2)
            elif choise == "2":
                stand = True
                time.sleep(2)
            else:
                print("hit or stand")
                self.playing()

# setter alt klart med tankte på hvem som har vhilke kort
def begin():
    player.draw()
    dealer.draw()
    player.draw()
    dealer.draw()

#printer statusen, hvem har hva
def status():
    print("dealer shows card")
    print(dealer.cards[0])
    print(f"player cards")
    print(f"{player.cards} value: {player.getPoints()}")


def whowins():
    scoreDealer = dealer.getPoints()
    scorePlayer = player.getPoints()
    time.sleep(1)
    if scorePlayer == scoreDealer:
        print(f"player score: {player.points}\ndealer score: {dealer.points}\nLOL")
    elif scoreDealer < scorePlayer and scoreDealer < 22 and scorePlayer <22 or scoreDealer > 21:
        print(f"YOU WIN!!")
    elif scoreDealer > scorePlayer and scoreDealer < 22 and scorePlayer <22 or scorePlayer > 21:
        print("YOU LOSE")
    elif scoreDealer > 21 and scorePlayer > 21:
        print(f"player score: {player.points}\ndealer score: {dealer.points}\nLOL")


def again():
    global gaming
    print(f"play again press ENTER")
    string = input()
    if string != "":
        gaming = False





#bygger spillet       
deck = Cards()
deck.nykortstokk()
deck.shuffle()



gaming = True
print("WELCOME! to OBLIG_4 BY Adrian_Ditmasen BJ .;,,,;.\n")
while gaming == True:
    dealer = Cards()
    player = Cards()
    begin()
    status()
    player.playing()
    dealer.botHitter()
    whowins()
    again()
    




#while gaming == True:





