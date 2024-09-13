#Listen fra forrige oppgave
tolkienSineBøker = ["Farmer Giles og Ham", "Lord of The rings The Fellowship of the Ring", "Lord of The rings The Return of the King", "Lord of The rings The Two Towers", "The Adventures of Tom Bombadil", "The Hobbit", "The Silmarillion", "Tree and Leaf", "Unfinished Tales"]
tempListe = []
søkeord = "Lord of The rings"


#en måte å printe ut alle elementene som inneholder en stregn i lista:
print("en måte å gjøre det på")
for Bok in tolkienSineBøker:
    
    if søkeord in Bok:
        print(Bok)

#en annen måte å gjøre det på:
print("enda en måte å gjøre det på")
for bokTall in range(len(tolkienSineBøker)):
    
    if søkeord in tolkienSineBøker[bokTall]:
        print(tolkienSineBøker[bokTall])