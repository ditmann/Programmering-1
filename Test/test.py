all_wares = {
    "amd_processor": {
        "name": "AMD Ryzen 9 5900X Processor",
        "price": 5590.0,
        "number_in_stock": 50,
        "ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],
        "description": "All the cores and threads you'll need!",
    },
    "playstation_5": {
        "name": "PlayStation 5",
        "price": 5999.0,
        "number_in_stock": 0,
        "ratings": [5.0, 5.0, 4.5, 2.0, 5.0, 4.5, 4.0],
        "description": "Next generation console, never in stock!",
    },
    "hdmi_cable": {
        "name": "Belkin Ultra High Speed HDMI Cable - 2m",
        "price": 349.0,
        "number_in_stock": 3,
        "ratings": [5.0, 5.0, 4.5, 5.0, 5.0, 5.0],
        "description": "A high speed overprices HDMI cable!",
    }
}




def print_ware_information(ware):
    '''Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.'''
    for info in ware:
        print(f"{info}: {ware[info]}")

def get_all_wares_in_stock(all_wares):
    '''Returnerer en dictionary med alle varer som er på lager.'''
    stock = {}
    for wares, info in all_wares.items():
        if info["number_in_stock"] > 0:
            stock[wares] = info
    return stock



all_wares_in_stock = get_all_wares_in_stock(all_wares)
print(all_wares_in_stock)
for ware in all_wares_in_stock.values():
    print_ware_information(ware)