bill = []
total = 0

while True:
    item = input("Enter an item (or 'done' to finish): ")
    if item.lower() == 'done':
        break

    price = float(input(f"Enter the price for {item}: "))
    bill.append((item, price))
    total += price

print("\nReceipt:")
for item, price in bill:
    print(f"{item}: ₹{price:.2f}")
print(f"Total: ₹{total:.2f}")