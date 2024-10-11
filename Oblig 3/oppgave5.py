#lager dictionaries av filmene og setter de i en liste
lFilmer = [
    {"name": "inception", "year" : 2010, "rating" : 8.7,},
    {"name": "insideOut","year": 2015, "rating" :8.1,} ,
    {"name": "conAir", "year": 1997, "rating" :6.9},
    ]


#funksjon for åspørre om filmer så legge de til
def filmInfo():
    name = input("hva heter filmen?")
    year = int(input("hvilket år ble filmen utgitt?"))
    rating = float(input("fra 1-10 hvor god var den?"))
    nyFilm(name,year,rating,)

def nyFilm(name,year,rating):
    lFilmer.append({"name":name, "year": year, "rating":rating,})
    print(lFilmer)

filmInfo()