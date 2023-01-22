class Cat:

    def __init__(self, name="No name", age=0, gender="Undefined"):
        self.name = name
        self.age = age
        self.gender = gender

    def talk(self):
        print(f"Myau! My name is {self.name}")


class Dog:
    def talk(self):
        print("Gav!")


cat_1 = Cat("Garfield", 5, "Male")
print(cat_1.name, cat_1.age)
cat_2 = Cat("Murka", 3, "Female")
print(cat_2.name, cat_2.age, cat_2.gender)
cat_2.talk()
cat_1.talk()