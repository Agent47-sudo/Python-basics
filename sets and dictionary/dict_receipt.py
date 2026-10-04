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
if price < 0:
    print("Price cannot be negative. Please enter a valid price.")
elif price == 0:
    print("Free item?")
else:
    total = price + price2
    print("\nReceipt:")
    print(f"{bill['item']}: ₹{bill['price']:.2f}")
    print(f"{bill2['item']}: ₹{bill2['price']:.2f}")
    print(f"Total: ₹{total:.2f}")