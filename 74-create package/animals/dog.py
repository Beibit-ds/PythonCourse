from animals.animal import Animal

class Dog(Animal):
    def __init__(self, name="No name", age=0, breed="Undefined"):
        Animal.__init__(self, name, age)
        self.breed = breed

    def talk(self):
        print("Gav! ", end="")
        Animal.talk(self)

    def run(self):
        print(f"Hi, I am {self.name} and I am running...")
