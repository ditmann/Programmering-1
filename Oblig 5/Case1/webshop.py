from wallet import Wallet

def print_ware_information(ware):
    '''Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.'''
    for info in ware:
        print(f"{info}: {ware[info]}")


def calculate_average_ware_rating(ware):
    '''Returnerer den gjennomsnittlige ratingen for en spesifisert vare.'''
    rating = 0
    n = 0
    for number in ware["ratings"]:
        rating += number
        n += 1
    return rating/n

def get_all_wares_in_stock(all_wares):
    '''Returnerer en dictionary med alle varer som er på lager.'''
    stock = {}
    for wares, info in all_wares.items():
        if info["number_in_stock"] > 0:
            stock[wares] = info
    return stock


def is_number_of_ware_in_stock(ware, number_of_ware):
    '''Returnerer en Boolean-verdi som representerer om et spesifisert antall av
    en gitt vare finnes på lager.'''
    if ware["number_in_stock"] >= number_of_ware:
        return True
    else:
        return False


def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware=1):
    '''Legger til et spesifisert antall av en gitt vare i en spesifisert
    handlevogn.'''
    inStock = is_number_of_ware_in_stock(ware, number_of_ware)
    if inStock == True:
        shopping_cart[ware_key] = ware
        ware["number_in_stock"] = number_of_ware
    else:
        print(f"only {ware["number_in_stock"]} left of: {ware_key}, you asked for {number_of_ware}")


def calculate_shopping_cart_price(shopping_cart, all_wares, tax=1.25):
    '''Returnerer prisen av en handlevogn basert på varene i den.'''
    totalPrice = float(0)
    for things in shopping_cart:
        numberWanted = all_wares[things]["number_in_stock"]
        price = all_wares[things]["price"]
        while numberWanted > 0:
            totalPrice += price
            numberWanted -= 1  
    return totalPrice*tax

def can_afford_shopping_cart(shopping_cart_price, wallet):
    '''Returnerer en Boolean-verdi basert på om det er nok penger i en gitt
    lommebok for å kjøpe en handlevogn.'''
    if shopping_cart_price <= Wallet.get_amount(wallet):
        return True
    else:
        return False

def buy_shopping_cart(shopping_cart, all_wares, wallet):
    '''Kjøper varene i en handlevogn. Parameterene defineres i oppgaven.'''
    totalPrice = calculate_shopping_cart_price(shopping_cart, all_wares)
    affordable = can_afford_shopping_cart(totalPrice,wallet)
    if affordable == True:
        Wallet.subtract_amount(wallet, totalPrice)
    else:
        print(f"insufficient funding, wallet: {Wallet.get_amount(wallet)}, cart price: {totalPrice}")

#------------------------------------------
# Predefinerte funksjoner
#------------------------------------------
def is_ware_in_stock(ware):
    '''Returnerer en Boolean-verdi som representerer om en vare er på lager.'''
    if ware["number_in_stock"] >= 1:
        return True
    else:
        return False

def clear_shopping_cart(shopping_cart):
    '''Tømmer en handlevogn.'''
    shopping_cart.clear()
