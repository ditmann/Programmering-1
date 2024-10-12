#""" 
# Dette er mest spagetti kode jeg har laget noen gang
#"""



#lager dictionaries av filmene og setter de i en liste
lFilmer = [
    {"name": "inception", "year" : 2010, "rating" : 8.7,},
    {"name": "insideOut","year": 2015, "rating" :8.1,} ,
    {"name": "conAir", "year": 1997, "rating" :6.9},
    ]


#funksjon for åspørre om filmer så legge de til
def filmInfo():
    name = input("hva heter filmen?")
    year = int(input("hvilket år ble filmen utgitt? (må være heltall)"))
    rating = float((input("fra 1-10 hvor god var den? (må være tall, 0 = har ikke rating)")))
    if rating == 0:
        rating = 5
    nyFilm(name,year,rating,)

def nyFilm(name,year,rating):
    lFilmer.append({"name":name, "year": year, "rating":rating,})
    print(lFilmer)

#kaller på legg til filmer
filmInfo()


#printer ut filmer i en setning med info
def utskrift():
    for movies in lFilmer:
        print(f"{movies["name"]} - {movies["year"]} has a rating of {movies["rating"]}")

#regner regner ut gjenomsnittlig rating og returnerer det
def gjennomRating():
    ratingSUM = 0
    n=0 
    for movies in lFilmer:
        ratingSUM = ratingSUM + movies["rating"]
        n= n + 1 
    return(ratingSUM/n)

#tar inn en liste og årstall og lager en ny liste med filmer fra det året
def filmerÅr(liste,år):
    nyliste = []
    for filmer in liste:
        if filmer["year"] == år:
            nyliste.append(filmer)
    return(nyliste)


#sender inn en liste med filmer og år så får alle filmene fra det året ut
print(filmerÅr(lFilmer,2010))

#kaller på gjennomsnitts funksjonen
gjennomsnitt = gjennomRating()
print(gjennomsnitt)

#leser av en fil og skriver det ut i terminal
def lesFil(filnavn):
    with open(filnavn, mode="r") as f:
        info = f.read()
    print(info)


#lager text fil og skriver i den
def skrivTiltxt(liste,filnavn):
    with open(f"{filnavn}.txt",mode="wt")as f:
        for movies in liste:
            f.write(f"{movies["name"]} - {movies["year"]} has a rating of {movies["rating"]}\n")
    lesFil(f"{filnavn}.txt")

#sender liste og navn på txt fil til funksjon
skrivTiltxt(lFilmer,"gaming")







