recharge = float(input("Enter recharge amount: "))
data_gb = float(input("Enter data (in GB): "))

if recharge > 399 and data_gb > 2:
    print("Extra bonus applied")
else:
    print("No bonus")