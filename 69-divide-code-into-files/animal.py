class Animal:
    def __init__(self, name="No name", age=0):
        self.name = name
        self.age = age

    def say_age(self):
        print(f"I am {self.age}")

    def talk(self):
        print(f"My name is {self.name}")

