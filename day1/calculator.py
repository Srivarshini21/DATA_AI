print("CLI Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Result:", a + b)

if choice == 2:
    print("Result:", a - b)

if choice == 3:
    print("Result:", a * b)

if choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Division not possible")
