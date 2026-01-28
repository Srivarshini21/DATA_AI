
correct_pin="1234"
max_attempts=3

print("Insert ATM card")

for attempt in range(1, max_attempts + 1):
	pin=input("Enter PIN: ")

	if pin==correct_pin:
		print("Login successful")
		break
	else:
		if attempt==max_attempts:
			print("Account blocked")
		else:
			print("Invalid credentials")