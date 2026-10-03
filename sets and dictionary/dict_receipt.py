item = input("Enter the item name: ").strip().title()
item2 = input("Enter the second item name: ").strip().title()
price = float(input("Enter the price: "))
price2 = float(input("Enter the second price: "))

bill = {
    "item": item,
    "price": price
}

bill2 = {
    "item": item2,
    "price": price2
}


print(f"\n-------RECEIPT-------\nItem: {bill['item']}\nPrice: ₹{bill['price']:.2f}\n---------------------")
print(f"\n-------RECEIPT-------\nItem: {bill2['item']}\nPrice: ₹{bill2['price']:.2f}\n---------------------")