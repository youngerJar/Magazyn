Milk = {"Name":"Milk",
         "Quantity":"120",
         "Unit":"L",
         "Unit_price":"PLN"}
Mug = {"Name":"Mug",
         "Quantity":" 30",
         "Unit":"szt",
         "Unit_price":"PLN"}
Farba = {"Name":"Farb",
       "Quantity":"3000",
       "Unit":"L",
       "Unit_price":"PLN"}
items =[Milk, Mug, Farba]
headers = ("Name\tQuantity\tUnit\tUnit Price (PLN)")
sold_items= []
def get_items():
    print(headers)
    for i in items:
        print(i["Name"],i["Quantity"],i["Unit"],i["Unit_price"])

word = input("What would you like to do?")
while word != "exit":
    if word =="show":
        get_items()
        word = input("What would you like to do?")
else:
    print("Exiting, bye!")


