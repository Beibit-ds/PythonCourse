from animal import Animal

class Cat(Animal):
    def __init__(self, name="No name", age=0, gender="Undefined"):
        Animal.__init__(self, name, age)
        self.gender = gender

    def talk(self):
        print("Myau! ", end="")
        Animal.talk(self)