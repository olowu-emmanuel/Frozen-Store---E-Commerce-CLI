# Frozen Store 🛒

This is a Python command-line interface (CLI) application I built to simulate a fully functional E-commerce shopping cart. 

It starts off with a quick age verification check (you have to be 18 or older to shop). Once you are in, it drops you into an interactive menu where you can browse products, manage your cart, apply discount codes, and check out—all directly from the terminal.

# What it does
* Age Gate:** Checks your age before granting access to the main store.
* Inventory System:** Displays available products, prices (in Naira ₦), and actively tracks stock levels so you can't buy what isn't there.
* Cart Management:** You can add items, update quantities, remove items, and view your current subtotal at any time.
* Discount System:** Accepts specific promo codes (like `SAVE10` or `FIRSTBUY`) to give percentage-based discounts on your order.
* Checkout System:** Calculates your final total by applying discounts and an 8% tax, then automatically deducts the purchased items from the store's overall stock.

# How to run it locally
If you want to try it out on your own machine, just clone the repository and run the Python file. 

Using your terminal (assuming you save the file as `store.py`):
```bash
python store.py
