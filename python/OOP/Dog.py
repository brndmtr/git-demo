class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks:{sound}"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

#print(miles.species)
#print(buddy.name)
#print(jack)
#print(jim.speak("woof"))
#print(type(miles))
#print(isinstance(miles, Dog))
#print(isinstance(miles, Bulldog))
print(jim.speak("Woof"))
print(miles.speak("Grr"))