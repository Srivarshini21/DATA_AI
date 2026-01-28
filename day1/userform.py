print("User Registration Form")

name = input("Enter name: ")
age = input("Enter age: ")
email = input("Enter email: ")
password = input("Enter password: ")

if len(name) < 3:
    print("Invalid name (minimum 3 characters)")
else:
    print("Name valid")

if age.isdigit() and int(age) >= 18:
    print("Age valid")
else:
    print("Invalid age (must be 18 or above)")

if "@" in email and "." in email:
    print("Email valid")
else:
    print("Invalid email")

if len(password) >= 8:
    print("Password valid")
else:
    print("Invalid password (minimum 8 characters)")