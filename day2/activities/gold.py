
bill = float(input("Enter billing amount: "))
weekend = input("Came on weekend? (yes/no): ").strip().lower()
gold_member = input("Gold member? (yes/no): ").strip().lower()

is_weekend = weekend in ("yes", "y")
is_gold_member = gold_member in ("yes", "y")

if bill > 1000 and is_weekend and is_gold_member:
	discount = bill * 0.20
	final_amount = bill - discount
	print("Eligible for 20% offer")
	print(f"Discount: {discount}")
	print(f"Final bill: {final_amount}")
else:
	print("Not eligible for offer")
	print(f"Final bill: {bill}")

