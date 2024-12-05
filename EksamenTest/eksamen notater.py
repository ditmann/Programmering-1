import json  # Importer JSON-modulen som lar oss jobbe med JSON-data

# Eksempel på bestilling
order = {
    "ribbe": 3,
    "pinnekjøtt": 2,
    "lutefisk": 1,
    "nøttestek": 0,
    "reinstyrstek": 1,
}

# Funksjon for å lagre bestilling i JSON-fil
def save_order_to_json(order, filename="order_history.json"):
    # Åpner en fil i skrive-modus ('w' for write)
    with open(filename, "w") as file:
        # Konverterer bestillingen til JSON-format og skriver den til filen
        json.dump(order, file, indent=4)  # 'indent=4' sørger for pen formatering av JSON-data

def load_order_from_json(filename="order_history.json"):
    try:
        # Åpner en fil i lese-modus ('r' for read)
        with open(filename, "r") as file:
            # Leser JSON-dataene fra filen og konverterer det tilbake til et Python-objekt
            return json.load(file)  # Returnerer bestillingen som et Python-dictionary
    except FileNotFoundError:
        # Håndterer tilfeller hvor filen ikke finnes
        print(f"Feil: Finner ikke filen '{filename}'.")
        return None
#--------------------------------------------------------------------------
users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }

# Iterer over alle brukernavn og tilhørende brukerinfo i users-dictionaryen
for username, user_info in users.items():
    # Skriv ut brukernavnet
    print(f"\nUsername: {username}")
    
    # Kombiner fornavn og etternavn til et fullstendig navn
    full_name = f"{user_info['first']} {user_info['last']}"
    # Hent plasseringen til brukeren
    location = user_info['location']
    
    # Skriv ut fullt navn med første bokstav stor for hvert navn
    print(f"\tFull name: {full_name.title()}")
    # Skriv ut plasseringen med første bokstav stor
    print(f"\tLocation: {location.title()}")














#---------------------------------------------------------
# Lager en liste over motorsykler
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

# Skriver ut hele listen over motorsykler
print(motorcycles)
# Output: ['honda', 'yamaha', 'suzuki', 'ducati']

# Definerer en variabel for å holde motorsykkelmerket som er for dyrt
too_expensive = 'ducati'

# Fjerner den dyre motorsykkelen fra listen
motorcycles.remove(too_expensive)

# Skriver ut listen etter at den dyre motorsykkelen er fjernet
print(motorcycles)
# Output: ['honda', 'yamaha', 'suzuki']

# Skriver ut en melding som sier at motorsykkelen er for dyr
print(f"\nA {too_expensive.title()} is too expensive for me.")
# Output: A Ducati is too expensive for me.

# Bruke pop() med en indeks for å fjerne og returnere et spesifikt element i listen
index_to_remove = 0  # Indeksen til elementet som skal fjernes
removed_motorcycle = motorcycles.pop(index_to_remove)

# Skriver ut listen etter å ha brukt pop() med en indeks
print(motorcycles)
# Output: ['yamaha', 'suzuki']

# Skriver ut motorsykkelen som ble fjernet med pop()
print(f"\nThe motorcycle removed using pop() was a {removed_motorcycle.title()}.")
# Output: The motorcycle removed using pop() was a Honda.
#--------------------------------------------------------------------------------
class BankAccount:
    """En enkel klasse for å representere en bankkonto."""

    def __init__(self, owner, balance=0.0):
        """
        Initialiserer en ny bankkonto.
        
        :param owner: Navnet på eieren av kontoen
        :param balance: Startbalansen til kontoen (standard er 0.0)
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Setter inn penger på kontoen.
        
        :param amount: Beløpet som skal settes inn
        """
        if amount > 0:
            self.balance += amount
            print(f"{amount} har blitt satt inn på kontoen.")
        else:
            print("Beløpet må være positivt for å sette inn penger.")

    def withdraw(self, amount):
        """
        Tar ut penger fra kontoen hvis nok midler er tilgjengelig.
        
        :param amount: Beløpet som skal tas ut
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} har blitt tatt ut fra kontoen.")
        else:
            print("Ugyldig beløp eller utilstrekkelige midler.")

    def get_balance(self):
        """
        Returnerer nåværende balanse på kontoen.
        
        :return: Kontobalansen
        """
        return self.balance

    def __str__(self):
        """
        Returnerer en strengrepresentasjon av bankkontoen.
        
        :return: Strengrepresentasjon av kontoen
        """
        return f"BankAccount(owner: {self.owner}, balance: {self.balance:.2f})"

# Eksempel på bruk av BankAccount-klassen
konto = BankAccount("Ola Nordmann", 1000.0)
print(konto)  # Output: BankAccount(owner: Ola Nordmann, balance: 1000.00)

konto.deposit(500.0)
print(konto.get_balance())  # Output: 1500.0

konto.withdraw(200.0)
print(konto.get_balance())  # Output: 1300.0

print(konto)  # Output: BankAccount(owner: Ola Nordmann, balance: 1300.00)
#--------------------------------------------------------------------