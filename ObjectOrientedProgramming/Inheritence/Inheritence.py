class Animal:
    def __init__(self, name):
        self.name = name
        self.greeting = {"greeting": ("Hello, I'm %s." % self.name)}

    def speak(self):
        raise NotImplementedError("Subclass not implemented abstract method")

    def eat(self):
        raise NotImplementedError("Subclass not implemented abstract method")

    def walk(self):
        print(self.name + " performs a movement")

    def factory(species, name):
        animals = {"Goose": Goose(name), "Cat": Cat(name), "Dog": Dog(name), "Bear": Bear(name),
                   "Human": Human(name), "Velociraptor": Velociraptor(name)}
        return animals[species]


class Goose(Animal):
    def speak(self):
        print(self.greeting["greeting"] + " HONK!")

    def eat(self):
        print("peck peck peck")
        

class Cat(Animal):
    def speak(self):
        print(self.greeting["greeting"] + " Meow")

    def eat(self):
        print("#Eats suspiciously#")


class Dog(Animal):
    def speak(self):
        print(self.greeting["greeting"] + " Bork Bork")

    def eat(self):
        print("Chew")
        

class Bear(Animal):
    def speak(self):
        print(self.greeting["greeting"] + " Roar")

    def eat(self):
        print("Tearrr!!")
        

class Human(Animal):
    def speak(self):
        print(self.greeting["greeting"] + " Wazzahhuppp")

    def eat(self):
        print("Monch Monch")
        

class Velociraptor(Animal):
    def speak(self):
        print(self.greeting["greeting"] + " Skrrrrttt")

    def eat(self):
        print("bite bite")


Animal("Gary")
my_cat = Animal.factory("Cat", "Gary")
my_cat.speak()