
# Simple Restaurant Ordering System (CLI)

menu = {
	1: ("Biryani", 250),
	2: ("Fried Rice", 180),
	3: ("Noodles", 170),
	4: ("Burger", 120),
	5: ("Pizza", 300),
}

name = input("Enter customer name: ").strip().upper()
weekend = input("Came on weekend? (yes/no): ").strip().lower()
gold = input("Gold member? (yes/no): ").strip().lower()

is_weekend = weekend in ("yes", "y")
is_gold = gold in ("yes", "y")

cart = {} 

while True:
	print("\n--- MENU ---")
	for item_id in menu:
		item_name, price = menu[item_id]
		print(f"{item_id}. {item_name} - {price}")
	print("Type item number to add")
	print("Type Done to finish")

	choice = input("Enter choice: ").strip()
	if choice.lower() == "done":
		break

	if not choice.isdigit() or int(choice) not in menu:
		print("Invalid choice")
		continue

	qty = input("Enter quantity: ").strip()
	if not qty.isdigit() or int(qty) <= 0:
		print("Invalid quantity")
		continue

	item_id = int(choice)
	cart[item_id] = cart.get(item_id, 0) + int(qty)
	print("Added to cart")

if len(cart) == 0:
	print("Cart is empty")	
else:
	print("\n--- BILL RECEIPT ---")
	print("Customer:", name)
	print("Weekend:", "YES" if is_weekend else "NO")
	print("Gold Member:", "YES" if is_gold else "NO")
	print("\nItem\t\tQty\tPrice\tTotal")

	subtotal = 0
	for item_id in cart:
		item_name, price = menu[item_id]
		qty = cart[item_id]
		total = price * qty
		subtotal += total
		print(f"{item_name}\t{qty}\t{price}\t{total}")

	discount = 0
	if subtotal > 1000 and is_weekend and is_gold:
		discount = subtotal * 0.20

	final_total = subtotal - discount
	print("\nSubtotal:", subtotal)
	print("Discount:", discount)
	print("Final Total:", final_total)