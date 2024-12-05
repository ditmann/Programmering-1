menu = {
    "ribbe":float(145.90),
    "pinnekjøtt":float(155.9),
    "lutefisk":float(135.90),
    "nøttestek":float(135.9),
    "reinstyrstek":float(155.9),
}
order_history = []

def display_menu_item(menu,menu_item):
    print(f"Menu:\n{menu_item}: {menu[menu_item]},-")
    

def place_order(ribbe=0,pinne=0,lute=0,nut=0,rein=0,):
    order={
        "ribbe":ribbe,
        "pinnekjøtt":pinne,
        "lutefisk":lute,
        "nøttestek":nut,
        "reinstyrstek":rein,    
    }
    if rein > 0:
        print("Buhuu")

    return order

def calculate_total(menu,order):
    cost = 0
    for item in menu:
        if order[item]>0:
            cost += menu[item] * order[item]
    
    return cost

def display_cost(menu,order):
    for item in menu:
        cost = 0
        if order[item]>0:
            cost += menu[item] * order[item]
            print(f"{item}-({order[item]})-{cost}")
            
            

def confirm_order(order_cost):
    print(f"det blir {order_cost},-")
    yesno = input("vil du ha ordren yes/no")
    if yesno == "yes":
        print("rudolf er grønn på nesen!")
        return True
    elif yesno == "no":
        print("rudolf er rød på nesen!")
        return False
        
def record_order(history, order):
    history.append(order)

def save_order_to_file(file_name,order):
    with open(file_name,"w") as file:
        json.dump(order,file,indent = 4)
        

def load_order_from_file(file_name):
    try:
        with open(file_name,"r") as file:
            return json.load(file)
    except:
        print("du denne filen finnes ikke")
        return None
    