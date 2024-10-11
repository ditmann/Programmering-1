
#liste med 3 dictionaries
brettspill = [
    {"tittel" : "Dixit", "spilletid" : 30, "aldersgrense" : 8,"år": 2008,},
    {"tittel": "pandemic", "spilletid": 45, "aldersgrense": 8, "år": 2008},
    {"tittel": "wingspan", "spilletid": 40, "aldersgrense": 10, "år": 2019},
]

for spill in brettspill:
    print(f"{spill["tittel"]} er ment for spillere far {spill["aldersgrense"]} år og oppover")


brettspill.append({"title" : "mysterium", "spillertid": 42, "andersgrense": 10, "år":2015,})

print(brettspill)