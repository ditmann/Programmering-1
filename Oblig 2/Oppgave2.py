#lager liste med tall 9-101
listeMedTall = []
n = 9
while n <= 101:
    listeMedTall.append(n)
    n=n+1




#ser etter partal og lager liste med odetallene

print("liste med odetall for løkke:".title())
oddetall = []
for tall in listeMedTall:
    rest = tall % 2
    if rest != 0:
        oddetall.append(tall)
print(oddetall)



#skal gjøre det samme med while løkke

print("liste med odetall while løkke:".title())
odetall2 = []
nummer = 9
while nummer <= 101:
    restW = nummer % 2
    if restW != 0:
        odetall2.append(nummer)
    nummer = nummer+1
print(odetall2)