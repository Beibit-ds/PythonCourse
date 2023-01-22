class Animal:
    def __init__(self, name="No name", age=0):
        self.name = name
        self.age = age

    def say_age(self):
        print(f"I am {self.age}")


class Cat(Animal):
    def __init__(self, name="No name", age=0, gender="Undefined"):
        Animal.__init__(self, name, age)
        self.gender = gender

    def talk(self):
        print(f"Myau! My name is {self.name}")


class Dog(Animal):
    def __init__(self, name="No name", age=0, breed="Undefined"):
        Animal.__init__(self, name, age)
        self.breed = breed

    def talk(self):
        print(f"Gav! My name is {self.name}. I am {self.breed}.")

    def run(self):
        print(f"Hi, I am {self.name} and I am running...")


dog_1 = Dog(name="Rex", age=3, breed="Bulldog")
dog_2 = Dog(name="Laika", age=13, breed="German Shepherd")
dog_1.talk()
dog_2.run()