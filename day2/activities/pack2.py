import package


print(
	"MENU\n"
	" 1. Area of Circle\n"
	" 2. Circumference of Circle\n"
	" 3. Area of Rectangle\n"
	" 4. Perimeter of Rectangle\n"
	" 5. Area of Triangle\n"
	" 6. Perimeter of Triangle"
)

op = int(input("Enter operation to be performed: "))

if op == 1:
	r = float(input("Enter radius: "))
	print(package.area_circle(r))
elif op == 2:
	r = float(input("Enter radius: "))
	print(package.circumference_circle(r))
elif op == 3:
	l = float(input("Enter length: "))
	w = float(input("Enter width: "))
	print(package.area_rectangle(l, w))
elif op == 4:
	l = float(input("Enter length: "))
	w = float(input("Enter width: "))
	print(package.perimeter_rectangle(l, w))
elif op == 5:
	b = float(input("Enter base: "))
	h = float(input("Enter height: "))
	print(package.area_triangle(b, h))
elif op == 6:
	s1 = float(input("Enter side1: "))
	s2 = float(input("Enter side2: "))
	s3 = float(input("Enter side3: "))
	print(package.perimeter_triangle(s1, s2, s3))
else:
	print("Invalid")

