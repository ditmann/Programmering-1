
#spør om et tall hvis ikke det er et tall spør den på nytt
def spørsmål():
    global svar
    try:
        svar = int(input("Hva er svaret på livet, universet og alle ting? Hint: Det er ett tall"))
    except:
        print("nå må du se på hintet")
        spørsmål()

#spør det vanskelige spørsmålet
spørsmål()

#tester svaret
if svar == 42:
    print("Det stemmer, meningen med liver er 42!")

elif svar > 30 and svar < 50:
    print("Nærmere, men feil")

else:
    print("FEIL")
    