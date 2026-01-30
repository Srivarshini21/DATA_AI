PRICE_PER_ITEM = 120  
try:
    items = int(input("How many items do you want to order? "))

    if items == 0:
        raise ZeroDivisionError("Zero items not allowed")

    total_bill = items * PRICE_PER_ITEM

except ValueError:
    print("Invalid input! Please enter a number.")

except ZeroDivisionError:
    print("You cannot order 0 items.")

else:
    print(f"Order placed successfully!")
    print(f"Total bill: ₹{total_bill}")

finally:
    print("Thank you for using Zomato!")