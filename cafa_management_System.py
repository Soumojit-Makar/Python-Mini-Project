#Defind the menu of restaurant 
menu={
    "Pizza":100,
    "Pasta":80,
    "Burger":120,
    "salad":70
}
list_of_order=list()
#Greet 
print("Welcome to Makar Restaurant")
for dis in menu:
    print(f"{dis}: Rs {menu.get(dis)}")
order_totle=0
while True:
    item=input("Enter the name of item you want to order : ")
    if item in menu:
        list_of_order.append(item)
        order_totle+=menu.get(item)
    else:
        print(f"Ordered item {item} is not avaialable yet!")
    anoter_order=input("Do you want to add anoter item? (Yes/No) ")
    if anoter_order == "No" or anoter_order == "no" or anoter_order == "n":
        break
for item in list_of_order:
    print(f" item name {item} : {menu.get(item)} ")
print(" Total amount is : ",order_totle)