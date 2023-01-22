from dog import Dog
from cat import Cat

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