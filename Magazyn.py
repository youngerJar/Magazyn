
Milk = {"Name":"Milk",
         "Quantity":"120",
         "Unit":"L",
         "Unit_price":"32"}
Kubek = {"Name":"Kubek",
         "Quantity":"23",
         "Unit":"szt",
         "Unit_price":"22"}
Farba = {"Name":"Farb",
       "Quantity":"3000",
       "Unit":"L",
       "Unit_price":"21"}
items =[Milk, Kubek, Farba]
headers = ("Name\tQuantity\tUnit\tUnit Price (PLN)")

def get_items():
    print(headers)
    for i in items:
        print(i["Name"],i["Quantity"],i["Unit"],i["Unit_price"])
def add_item():
    new_item = {}
    new_item["Name"]=input("Item Name: ")
    new_item["Quantity"]= input("Item Quantity: ")
    new_item["Unit"]= input("Item Unit: ")
    new_item["Unit_price"]= input("Item price: ")
    items.append((new_item))
def sell_item():
    sold_item ={}
    sold_item = ["Name"]= input("what prodyct to sell: ")
       
    
word = input("What would you like to do?")
while word != "exit":
    if word =="show":
        get_items()
        word = input("What would you like to do?")
    if word =="add":
        print("Adding to warehause:")
        add_item()
        word= input("What would you like to do?")
    if word =="sell":
        sell_item()
        word= input("What would you like to do?")
    
        
else:
    print("Exiting, bye!")


