def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_all(1, 2, 3, 4, 5)) 

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)