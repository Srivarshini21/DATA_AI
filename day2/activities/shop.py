
cart = []

while True:
	item = input("Add item to cart (type 'Done' to finish): ")

	if item.lower() == "done":
		break

	if item == "":
		print("Please enter an item name.")
		continue

	cart.append(item)
	print(f"Added: {item}")

print("\nCart Items:")
if len(cart) == 0:
	print("(cart is empty)")
else:
	for i in range(len(cart)):
		print(f"{i + 1}. {cart[i]}")
