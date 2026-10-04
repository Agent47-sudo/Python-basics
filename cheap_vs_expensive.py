item = input("Enter the item name: ").strip().title()
price = float(input("Enter the price: "))

thing = {
    "item": item,
    "price": price
}

if thing['price'] >=1000:
    print(f"{thing['item']} is expensive.")
else:
    print(f"{thing['item']} is cheap.")