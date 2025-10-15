# Intro
print("===================================")
print("       WELCOME TO FROZEN STORE     ")
print("===================================")

# Customer Details
CustomerName = input("Enter Your Name: ")
print(f"Hello {CustomerName}! HAPPY SHOPPING!")

# Product List (Dictionary)
products = {
    "P001": {"Name": "Laptop", "Price": 120000, "Stock": 100},
    "P002": {"Name": "Mouse", "Price": 7000, "Stock": 50},
    "P003": {"Name": "Keyboard", "Price": 15000, "Stock": 30},
    "P004": {"Name": "Monitor", "Price": 55000, "Stock": 25},
    "P005": {"Name": "Headset", "Price": 12000, "Stock": 40}
}

# Shopping Cart (List)
cart = []

# Discount Codes (Tuple)
discount_codes = (("SAVE10", 10), ("SAVE20", 20), ("FIRSTBUY", 15))
discount = 0

# Start Menu Loop
while True:
    print("\n========== ONLINE STORE MENU ==========")
    print("1. View Available Products")
    print("2. Add item to cart")
    print("3. View Cart")
    print("4. Update Item Quantity")
    print("5. Remove Item from Cart")
    print("6. Apply Discount Code")
    print("7. Checkout")
    print("8. Exit")
    
    choice = input("Enter Your Choice (1-8): ")

    # 1. View Available Products
    if choice == "1":
        print("\n--- AVAILABLE PRODUCTS ---")
        print("ID      Name         Price       Stock")
        print("---------------------------------------")
        for pid, details in products.items():
            name = details["Name"]
            price = details["Price"]
            stock = details["Stock"]
            print(f"{pid:<8}{name:<12}₦{price:<10}{stock}")

    # 2. Add Item to Cart
    elif choice == "2":
        product_id = input("Enter Product ID: ").upper()

        if product_id in products:
            product = products[product_id]
            if product["Stock"] == 0:
                print("❌ This product is out of stock.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("❌ Quantity must be greater than 0.")
                continue

            if quantity > product["Stock"]:
                print(f"❌ Only {product['Stock']} items available.")
                continue

            cart.append({
                "id": product_id,
                "name": product["Name"],
                "price": product["Price"],
                "qty": quantity
            })
            print(f"✅ Added {quantity} x {product['Name']} to cart.")
        else:
            print("❌ Invalid Product ID.")

    # 3. View Cart
    elif choice == "3":
        if not cart:
            print("\n🛒 Your cart is empty.")
        else:
            print("\n--- YOUR SHOPPING CART ---")
            print("Product         Qty     Price      Subtotal")
            print("-------------------------------------------")
            total = 0
            for item in cart:
                subtotal = item["price"] * item["qty"]
                total += subtotal
                print(f"{item['name']:<15}{item['qty']:<8}₦{item['price']:<10}₦{subtotal}")
            print("-------------------------------------------")
            print(f"Total: ₦{total}")

    # 4. Update Item Quantity
    elif choice == "4":
        if not cart:
            print("🛒 Cart is empty.")
            continue

        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['name']} (Qty: {item['qty']})")

        num = int(input("Enter item number to update: "))
        if 1 <= num <= len(cart):
            new_qty = int(input("Enter new quantity: "))
            pid = cart[num - 1]["id"]

            if new_qty <= 0:
                print("❌ Quantity must be greater than 0.")
                continue

            if new_qty <= products[pid]["Stock"]:
                cart[num - 1]["qty"] = new_qty
                print("✅ Quantity updated successfully.")
            else:
                print("❌ Not enough stock available.")
        else:
            print("❌ Invalid item number.")

    # 5. Remove Item from Cart
    elif choice == "5":
        if not cart:
            print("🛒 Cart is empty.")
            continue

        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['name']} (Qty: {item['qty']})")

        num = int(input("Enter item number to remove: "))
        if 1 <= num <= len(cart):
            removed = cart.pop(num - 1)
            print(f"✅ Removed {removed['name']} from cart.")
        else:
            print("❌ Invalid item number.")

    # 6. Apply Discount Code
    elif choice == "6":
        print("\nAvailable Codes:")
        for code, percent in discount_codes:
            print(f"{code} - {percent}% off")

        code_entered = input("Enter your discount code: ").upper()
        found = False
        for code, percent in discount_codes:
            if code_entered == code:
                discount = percent
                found = True
                print(f"✅ Discount code applied! ({discount}% off)")
        if not found:
            print("❌ Invalid discount code.")

    # 7. Checkout
    elif choice == "7":
        if not cart:
            print("🛒 Your cart is empty. Add items before checkout.")
            continue

        subtotal = sum(item["price"] * item["qty"] for item in cart)
        discount_amount = subtotal * (discount / 100)
        after_discount = subtotal - discount_amount
        tax = after_discount * 0.08
        total = after_discount + tax

        print("\n--- CHECKOUT SUMMARY ---")
        for item in cart:
            print(f"{item['name']} x{item['qty']} = ₦{item['price'] * item['qty']}")
        print("-------------------------------------------")
        print(f"Subtotal: ₦{subtotal}")
        print(f"Discount ({discount}%): -₦{discount_amount:.2f}")
        print(f"After Discount: ₦{after_discount:.2f}")
        print(f"Tax (8%): ₦{tax:.2f}")
        print(f"TOTAL: ₦{total:.2f}")

        confirm = input("Confirm purchase? (yes/no): ").lower()
        if confirm == "yes":
            for item in cart:
                products[item["id"]]["Stock"] -= item["qty"]
            cart.clear()
            discount = 0
            print("✅ Purchase complete! Thank you for shopping at Frozen Store.")
        else:
            print("❌ Checkout cancelled.")

    # 8. Exit
    elif choice == "8":
        print("\n👋 Thank you for visiting FROZEN STORE. Goodbye!")
        break

    # Invalid Choice
    else:
        print("❌ Invalid choice, please select a number between 1 and 8.")
