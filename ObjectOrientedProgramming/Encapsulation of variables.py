class Student:
    def __init__(self, name, age, superpower, favourite_colour):
        self.name = name
        self.age = age
        self.superpower = superpower
        self.favourite_colour = favourite_colour

    def __str__(self):
        output = "\nName: %s\nAge: %s\nSuperpower: %s\nFav Colour: %s" % (self.get_name(), self.get_age(), self.get_superpower(),self.favourite_colour)
        return output

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.name = age

    def get_superpower(self):
        return self.superpower

    def set_superpower(self, superpower):
        self.name = superpower

    def get_favourite_colour(self):
        return self.favourite_colour

    def set_favourite_colour(self, favourite_colour):
        self.name = favourite_colour


students = []

jack = Student("Jack", 16, "beating my meat", "period Red")
students.append(jack)
gabe = Student("Gabe", 9, "touching kids", "purple")
students.append(gabe)
amy = Student("Amy", 16, "speed", "blue")
students.append(amy)
owen = Student("Owen", 16, "teleportation", "orange")
students.append(owen)
print(students)

for a in students:
    print("Hi, I'm %s, my superpower is %s!!" % (a.get_name(), a.get_superpower()))

print(jack)