#Listen fra forrige oppgave
tolkienSineBøker = ["Farmer Giles og Ham", "Lord of The rings The Fellowship of the Ring", "Lord of The rings The Return of the King", "Lord of The rings The Two Towers", "The Adventures of Tom Bombadil", "The Hobbit", "The Silmarillion", "Tree and Leaf", "Unfinished Tales"]

#tom liste
tomListe = []


#litt usikker på om jeg tolker oppgaven riktig, men
tomListe.append(tolkienSineBøker[1])
tomListe.append(tolkienSineBøker[2])
tomListe.append(tolkienSineBøker[3])


#en måte å printe ut alle elementene i lista
for bøker in tomListe:
    print(bøker)


#en annen måte å kjøre det på
for nummer in range(len(tomListe)):
    print(tomListe[nummer])


