class Animal:
    def __init__(self, name="No name", age=0):
        self.name = name
        self.age = age

    def say_age(self):
        print(f"I am {self.age}")

    def talk(self):
        print(f"My name is {self.name}")


class Cat(Animal):
    def __init__(self, name="No name", age=0, gender="Undefined"):
        Animal.__init__(self, name, age)
        self.gender = gender

    def talk(self):
        print("Myau! ", end="")
        Animal.talk(self)

class Dog(Animal):
    def __init__(self, name="No name", age=0, breed="Undefined"):
        Animal.__init__(self, name, age)
        self.breed = breed

    def talk(self):
        print("Gav! ", end="")
        Animal.talk(self)

    def run(self):
        print(f"Hi, I am {self.name} and I am running...")


dog_1 = Dog(name="Rex", age=3, breed="Bulldog")
dog_2 = Dog(name="Laika", age=13, breed="German Shepherd")
cat_1 = Cat("Garfield", 5, "Male")
cat_2 = Cat("Murka", 3, "Female")
dog_1.talk()
dog_2.run()
cat_2.say_age()
cat_2.talk()
cat_1.talk()
dog_1.say_age()