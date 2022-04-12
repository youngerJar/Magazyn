Milk = {"Name":"Milk",
         "Quantity":"120",
         "Unit":"L",
         "Unit_price":"PLN"}
Mug = {"Name":"Mug",
         "quantity":"30",
         "unit":"szt",
         "unit_price":"PLN"}
Farba = {"Name":"Farba",
       "quantity":"3000",
       "unit":"L",
       "unit_price":"PLN"}
items =[Milk, Mug, Farba]
headers = ("Name\tQuantity\tUnit\tUnit Price (PLN)")
def get_items():
    print(headers)
    for i in items:
        print(i["Name"],)

word = input("What would you like to do?")
while word != "exit":
    if word =="show":
        get_items()
        word = input("What would you like to do?")
else:
    print("Exiting, bye!")


