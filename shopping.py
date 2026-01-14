# Read products from file
f = open("products.txt", "r")
lines = f.readlines()
f.close()

products = []
for line in lines:
    parts = line.strip().split(",")  # format: name,price,category
    if len(parts) == 3:
        products.append({"name": parts[0], "price": float(parts[1]), "category": parts[2]})

cart = []

while True:
    print("\nVELORA SHOP")
    print("1. View products")
    print("2. Add to cart")
    print("3. View cart")
    print("4. Filter price")
    print("5. Quit")

    choice = input("Pick (1-5): ")

    # 1. View products
    if choice == "1":
        print("\nPRODUCTS:")
        i = 1
        for p in products:
            print(str(i) + ". " + p['name'] + " - $" + str(p['price']) + " (" + p['category'] + ")")
            i += 1

    # 2. Add to cart
    elif choice == "2":
        print("\nPRODUCTS:")
        i = 1
        for p in products:
            print(str(i) + ". " + p['name'] + " - $" + str(p['price']))
            i += 1
        try:
            num = int(input("Product number: ")) - 1
            if num >= 0 and num < len(products):
                cart.append(products[num])
                print("Added " + products[num]['name'] + "!")
            else:
                print("Pick a valid product number")
        except:
            print("Type a number")

    # 3. View cart
    elif choice == "3":
        if not cart:
            print("\nCart empty")
        else:
            print("\nCART:")
            total = 0
            for item in cart:
                print("- " + item['name'] + " $" + str(item['price']))
                total += item['price']
            print("TOTAL: $" + str(total))

    # 4. Filter price
    elif choice == "4":
        try:
            low = float(input("Min price: "))
            high = float(input("Max price: "))
            print("\nProducts $" + str(low) + "-" + str(high) + ":")
            found = False
            for p in products:
                if low <= p['price'] <= high:
                    print("- " + p['name'] + " $" + str(p['price']))
                    found = True
            if not found:
                print("No products in this price range")
        except:
            print("Use numbers")

    # 5. Quit
    elif choice == "5":
        print("Thanks for shopping!")
        break

    else:
        print("Pick 1-5")