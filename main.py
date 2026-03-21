from itertools import product
import json
from json import JSONDecodeError
# inventory={}

try:
    with open(file="config.json", mode="r", encoding="utf-8") as file:
        inventory_data= json.load(file)
except (JSONDecodeError, FileNotFoundError, FileExistsError):
    inventory_data = []


# products={
#     "pomade":{"price":25,"quantity":20},
#     "lip Gloss":{"price":15,"quantity":30},
#     "face powder":{"price":40,"quantity":20},
#     "body spray":{"price":60,"quantity":15}
               
#     }



def add_product():
    products= input("Enter product name")
    price= float(input("Enter price: "))
    quantity=int(input("Enter quantity"))

    inventory_append ={"name":products,
                           "price":price, 
                           "quantity":quantity}
    inventory_data.append(inventory_append)
    with open(file="config.json", mode="w", encoding="utf-8") as file:
        json.dump(inventory_data, file, indent=4)


    print("product added surccessfully")

def view_inventory():
    print("inventory list:")

    for value in inventory_data:
        print(value)
 
        
def update_stock():
    products=input("Enter product name: " )
    if products in inventory_data:
        quantity=int(input("Enter new quantity: "))
        inventory_data[products]["quantity"]=quantity
        print("stock updated")
    else:
        print("product not found")


for product  in inventory_data: 
    if product["name"]:
        pass



def remove_product():
    products=input("Enter product name to remove: ")
    if products in inventory_data:
        del inventory_data[products]
        print("product removed")
    else:
        print("product not found")

def record_sale():
    products=(input("Enter product sold: "))
    qty=int(input("Enter quantity sold: "))

    if products in inventory_data:
        if inventory_data[products]["quantity"] >=qty:
            inventory_data[products]["quantity"] -=qty
            print("sale recorded")
        else:
            print("not enough stock")
    else:
        print("product not found")
while True:
    print("COSMETICS INVENTORY SYSTEM")
    print("1. View inventory")
    print("2. Add product")
    print("3. Update stock")
    print("4. Remove product")
    print("5. Record sale")
    print("6. Exist")

    choice=input("choose an option: ")
    if choice=="1":
        view_inventory()
    elif choice=="2":
        add_product()
    elif choice=="3":
        update_stock()
    elif choice=="4":
        remove_product()
    elif choice=="5":
        record_sale()
    elif choice=="6":
        break
    else:
        print("Invalid option")


