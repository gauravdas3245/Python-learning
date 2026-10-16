cart = {
    "Shirt": 599,
    "Jeans": 1299,
    "Shoes": 1999
}

total = 0

for item, price in cart.items():
    print(item, ":", price)
    total += price

print("Total cost:", total)