name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
profession = input("Enter your profession: ")   
def generate_profile(**kwargs):
    profile = f"Name: {kwargs['name']}\nAge: {kwargs['age']}\nCity: {kwargs['city']}\nProfession: {kwargs['profession']}"
    return profile 
print("\nGenerated Profile:")
print(generate_profile(name=name, age=age, city=city, profession=profession))