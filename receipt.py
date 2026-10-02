item = input("Enter the item name: ").strip().title()
item2 = input("Enter the second item name: ").strip().title()
price = float(input("Enter the price: "))
price2 = float(input("Enter the price of the second item: "))
print(f"\n-------RECEIPT-------\nItem: {item}\nPrice: ₹{price:.2f}\nItem: {item2}\nPrice: ₹{price2:.2f}")
total = price + price2
print(f"Total: ₹{total:.2f}\n---------------------")