class Person:
    def __init__(self, name):
        self.name = name

    def speak(self,  speech):
        print(speech)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


cloud = Person("Cloud")
tifa = Person("Tifa")
aeris = Person("Aeris")

cloud.speak(cloud.get_name())
tifa.speak(tifa.get_name())
aeris.speak(aeris.get_name())

cloud.set_name("Sephiroth")
cloud.speak("I recently changed my name to " + cloud.get_name())
