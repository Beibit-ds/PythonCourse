class Cat:
    def talk(self):
        print("Myau!")


class Dog:
    def talk(self):
        print("Gav!")


cat = Cat()
dog = Dog()
cat.name = "Garfield"
cat.age = 5
dog.name = "Rex"
cat.talk()
dog.talk()