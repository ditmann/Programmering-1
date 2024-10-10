#lager dictionaries av filmene og setter de i en liste
inception = {"year" : 2010, "rating" : 8.7,}
insideOut = {"year": 2015, "rating" :8.1,}
conAir = {"year": 1997, "rating" :6.9}
lFilmer = [inception,insideOut,conAir]




#funksjon for åspørre om filmer så legge de til
def filmInfo():
    name = input("hva heter filmen?")
    year = int(input("hvilket år ble filmen utgitt?"))
    rating = float(input("fra 1-10 hvor god var den?"))
    nyFilm(name,year,rating,)

def nyFilm(name,year,rating):
    

