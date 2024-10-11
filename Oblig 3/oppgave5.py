#lager dictionaries av filmene og setter de i en liste
lFilmer = [
    {"name": "inception", "year" : 2010, "rating" : 8.7,},
    {"name": "insideOut","year": 2015, "rating" :8.1,} ,
    {"name": "conAir", "year": 1997, "rating" :6.9},
    ]


#funksjon for åspørre om filmer så legge de til
def filmInfo():
    name = input("hva heter filmen?")
    year = (input("hvilket år ble filmen utgitt?"))
    rating = (input("fra 1-10 hvor god var den?"))
    if rating == "":
        rating = 5
    nyFilm(name,year,rating,)

def nyFilm(name,year,rating):
    lFilmer.append({"name":name, "year": year, "rating":rating,})
    print(lFilmer)

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

gjennomsnitt = gjennomRating()
print(gjennomsnitt)





