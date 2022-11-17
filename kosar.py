
foods = []
prices = []
total = 0

while True:
    item = input("Írd be a termék nevét (írd be a 'kész' szót az összegzéshez): ")
    if item.lower() == "kész":
        break
    else:
        price = float(input(f"Írd be a termék árát {item}: "))
        foods.append(item)
        prices.append(price)

print("------ Kosarad ------")

for item in foods:
    print(item, end=", ")

for price in prices:
    total += price

print(f"\nÖsszesen: {total}Ft")