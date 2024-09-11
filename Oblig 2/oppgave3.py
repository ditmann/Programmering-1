#lager liste
tolkienSineBøker = ["The Hobbit","Farmer Giles og Ham","The Fellowship of the Ring","The Two Towers", "The Return of the King","The Adventures of Tom Bombadil","Tree and Leaf"]


antallBøker = len(tolkienSineBøker)

#NR 1 done
print("de to første bøkene i lista er '%s' og '%s' mens den siste boka er '%s'"%(tolkienSineBøker[0],tolkienSineBøker[1],tolkienSineBøker[6]))

#legger til bøker
tolkienSineBøker.append("The Silmarillion")
tolkienSineBøker.append("Unfinished Tales")


#legger til "Lord of the rings" foran bøkene
tolkienSineBøker[2] = "Lord of The rings " + tolkienSineBøker[2]
tolkienSineBøker[3] = "Lord of The rings " + tolkienSineBøker[3]
tolkienSineBøker[4] = "Lord of The rings " + tolkienSineBøker[4]


#sorterer lista så skriver ut lista

tolkienSineBøker.sort()
print(tolkienSineBøker)

