def print_name_and_age(animal):
    print(f"{animal['name']}, {animal['age']}")

def cat_talk(name):
    print(f"Myau, I am {name}")

def dog_talk(name):
    print(f"Gav, I am {name}")

cat = {
    "name": "Garfield",
    "age": 5
}
dog = {
    "name": "Rex",
    "age": 10
}
print_name_and_age(cat)
cat_talk(cat['name'])
print_name_and_age(dog)
dog_talk(cat['name'])
