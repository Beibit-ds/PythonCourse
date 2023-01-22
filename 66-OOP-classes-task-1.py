class Cat:

    def __init__(self, name="No name", age=0, gender="Undefined"):
        self.name = name
        self.age = age
        self.gender = gender

    def talk(self):
        print(f"Myau! My name is {self.name}")


class Dog:

    def __init__(self, name="No name", age=0, breed="Undefined"):
        self.name = name
        self.age = age
        self.breed = breed

    def talk(self):
        print(f"Gav! My name is {self.name}. I am {self.breed}.")

    def run(self):
        print(f"Hi, I am {self.name} and I am running...")


dog_1 = Dog(name="Rex", age=3, breed="Bulldog")
dog_2 = Dog(name="Laika", age=13, breed="German Shepherd")
dog_1.talk()
dog_2.run()