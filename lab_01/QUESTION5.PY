items = []
quantities = []
prices = []
total = 0

while True:
    item = input("Enter the name of the item (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price per item: "))
    
    items.append(item)
    quantities.append(quantity)
    prices.append(price)
    total += quantity * price

print("\nGrocery Bill")
print("Item\tQuantity\tPrice\tTotal")
for i in range(len(items)):
    item_total = quantities[i] * prices[i]
    print(f"{items[i]}\t{quantities[i]}\t\t{prices[i]:.2f}\t{item_total:.2f}")

print(f"\nTotal Bill: {total:.2f}")
