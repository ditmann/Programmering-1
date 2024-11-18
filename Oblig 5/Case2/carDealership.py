from datetime import date

class car:
    def __init__(self, brand, model, price, year, month, new, km):
        
        self.brand = brand # streng
        self.model = model # streng
        self.price = price # float
        self.year = year # int
        self.month = month # int
        self.new = new # int
        self.km = km # int
        #--------------------------------------------------------------------------------
        ### tenker at det kan være letter å putte inn funksjonene:
        
        def print_car_information(self):
            pass
        
        def get_car_age(self):
            #her kunne man også laget en ny atributt som "self.age"
            pass

        def calculate_total_price(self):
            #her kunne man også laget en ny atributt som "self.totalPrice"
            pass

        def create_car(self):
            #dette hadde jo bare blitt å lage et nytt objekt, hadde ikke trengt en egen funkjson
            pass

        def next_eu_control(self):
            #denne funksjonen kunne vært i klassen sin den bruker mye info fra klassen
            pass

        def is_new(self):
            #denne funksjonen ville jeg også hatt i klassen, men kalt den Get_New eller noe lignende. Det er jo noe som omgår objektet så tenker den passer seg i klassen
            pass
    

car_register = {
    "toyotaBZ4X": {
        "brand": "Toyota",
        "model": "Corolla",
        "price": 96_000,
        "year": 2012,
        "month": 8,
        "new": False,
        "km": 163_000
    },
    "pugeot408": {
        "brand": "Pugeot",
        "model": "408",
        "price": 330_000,
        "year": 2019,
        "month": 1,
        "new": False,
        "km": 40_000
    },
    "audiRS3": {
        "brand": "Audi",
        "model": "RS3",
        "price": 473_000,
        "year": 2022,
        "month": 2,
        "new": True,
        "km": 0
    },
}

NEW_CAR_REGISTRATION_FEE = 8745
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR_FEE = 1000

def print_car_information(car):
    for key, info in car.items():
        print(f"{key}: {info}")
    

def create_car(car_register, brand, model, price, year, month, new, km=0):
    carName = { 
        "brand": brand,
        "model": model,
        "price": price,
        "year": year,
        "month": month,
        "new": new,
        "km": km,
        }
    car_register[brand+model] = [carName]
    print(f"new car register{car_register}")


def get_car_age(car):
    nowYear = 2024
    carAge = nowYear-car["year"]
    return carAge

def next_eu_control(car):
   nowYear = 2024
   nextEuYear = car["year"]
   while nextEuYear < nowYear:
       nextEuYear += 2
   return date(nextEuYear,car["month"],1)  
 

def rent_car_monthly_price(car):
    price = (car["price"])*RENT_CAR_PERCENTAGE
    if car["new"] == True:
        price += RENT_NEW_CAR_FEE
    return round(price,2)

def calculate_total_price(car):
    carPrice = car["price"]
    carAge = get_car_age(car)
    if carAge <= 3:
        if car["new"] == True:
            carPrice += 10783
        carPrice += 6681
    elif carAge >= 4 and carAge <=11:
        carPrice += 4034
    elif carAge >= 12 and carAge <= 29:
        carPrice += 1729
    return carPrice

def is_new(car):
    return car['new']

if __name__ == '__main__':
    create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)
    
    toyota = car_register['toyotaBZ4X']
    print_car_information(toyota)
    print(
        f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr."
    )
    print(
        f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}"
    )
    print(
        f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)}kr."
    )
    
    audi = car_register['audiRS3']
    print_car_information(audi)
    print(
        f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr."
    )
    print(
        f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}"
    )
    print(
        f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)}kr."
    )
