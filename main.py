from itertools import product
import json
from json import JSONDecodeError
import os
import sys

import shutil


# 1. SETUP PATHS
file_root = os.path.expanduser("~")
config_dir = os.path.join(file_root, "Documents", "config")
os.makedirs(config_dir, exist_ok=True)

inventory_file_path = os.path.join(config_dir, "config.json")


# 2. PYINSTALLER BUNDLE LOGIC (The "Fix")
def setup_user_files():
    """Copies bundled default JSONs to Documents/config if they don't exist."""
    if hasattr(sys, '_MEIPASS'):
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = os.path.abspath(".")
        
        

   
    files_to_setup = ["config.json"]
    
    for filename in files_to_setup:
        dest_path = os.path.join(config_dir, filename)
        if not os.path.exists(dest_path):
            source_path = os.path.join(bundle_dir, "config", filename)
            try:
                if os.path.exists(source_path):
                    shutil.copy(source_path, dest_path)
                else:
                    # Create an empty list file if no bundle source exists
                    with open(dest_path, "w", encoding="utf-8") as f:
                        json.dump([], f)
            except Exception as e:
                print(f"Initial setup error for {filename}: {e}")

 
setup_user_files()


try:
    with open(file=inventory_file_path, mode="r", encoding="utf-8") as subfile:
        inventory_data = json.load(subfile)
except (JSONDecodeError, FileNotFoundError):
    inventory_data = []



def main():
          
    while True:
        print("COSMETICS INVENTORY SYSTEM")
        print("1. View inventory")
        print("2. Add product")
        print("3. Update stock")
        print("4. Remove product")
        print("5. Record sale")
        print("6. Exist")

        choice=input("choose an option: ").strip()
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


def add_product():
    print("====== INVENTORY ======")
    products= input("Enter product name: \n")
    price= float(input("Enter price: \n"))
    quantity=int(input("Enter quantity: \n"))

    inventory_append ={"name":products,
                           "price":price, 
                           "quantity":quantity}
    inventory_data.append(inventory_append)

    with open(file=inventory_file_path, mode="w", encoding="utf8") as file:
            json.dump(inventory_data, file, indent=2)


    print("product added surccessfully")

def view_inventory():
    print("inventory list:")
    
    counter = 1
    for value in inventory_data:
        print(f"product no. {counter}")
        print(f'name: {value["name"]}')
        print(f'price: {value["price"]}')
        print(f'Quantity: {value["quantity"]}')
        counter +=1
        print()
        
 
        
def update_stock():
    products=input("Enter product name: " )
    if products in inventory_data:
        quantity=int(input("Enter new quantity: "))
        inventory_data[products]["quantity"]=quantity
        print("stock updated")
        with open(file=inventory_file_path, mode="w", encoding="utf8") as file:
            json.dump(inventory_data, file, indent=2)
    else:
        print("product not found")


    # for product  in inventory_data: 
    #     if product["name"]:
    #          pass



def remove_product():
    products=input("Enter product name to remove: ")
    if products in inventory_data:
        del inventory_data[products]
        print("product removed")

        with open(file=inventory_file_path, mode="w", encoding="utf8") as file:
            json.dump(inventory_data, file, indent=2)

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








if __name__ == "__main__":
    main()

input("Press Enter to exit ...")