import json

#åpner jason filen 
def lesJason(filnavn):
    try:
        with open(filnavn) as fil:
            dict_fra_fil = json.load(fil)
    except FileNotFoundError:
        print("filens finnes ikke n00B")
    else:
        return dict_fra_fil
    
    
#skriver til json filen
def skrivJason(filnavn,dictionary):
    try:
        with open(filnavn, "w") as fil:
            json.dump(dictionary, fil, indent = 4)
        
    except FileNotFoundError:
        print("fant ikke filen")
