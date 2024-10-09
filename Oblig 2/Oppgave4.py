#Listen fra forrige oppgave
tolkienSineBøker = ["Farmer Giles og Ham", "Lord of The rings The Fellowship of the Ring", "Lord of The rings The Return of the King", "Lord of The rings The Two Towers", "The Adventures of Tom Bombadil", "The Hobbit", "The Silmarillion", "Tree and Leaf", "Unfinished Tales"]
tempListe = []
søkeord = "Lord of The rings"

#en måte å printe ut alle elementene som inneholder en stregn i lista
for Bok in tolkienSineBøker:
    
    if søkeord.lower() in Bok.lower():
        print(Bok)


#måte 2 med indexer
for boktall in tolkienSineBøker:

    if søkeord in boktall:
        print(tolkienSineBøker)
    
    print(boktall)