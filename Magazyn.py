Milk = {"name":"Milk",
         "quantity":"120",
         "unit":"L",
         "unit_price":"PLN"}
Mug = {"name":"Coffy mug",
         "quantity":"30",
         "unit":"szt",
         "unit_price":"PLN"}
Farba={"name":"Farba",
       "quantity":"3000",
       "unit":"L",
       "unit_price":"PLN"}
items =[Milk, Mug, Farba]
headers = ["Name","Quantity","Unit","Unit Price (PLN)"]
def get_items():
  print(items)

word = input("What would you like to do?")
if word =="exit":
    print("Exiting...bye!")
    exit(1)
word = input("What would you like to do?")
if word =="show":
  get_items
  word = input("What would you like to do?")

