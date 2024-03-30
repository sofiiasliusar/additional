class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # def description(self):
    #     return f"{self.name} is {self.age} years old"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        # return f"{self.name} says {self.sound}"
        # there is no self sound - we access this parameter directly from a function
        return f"{self.name} says {sound}"
        

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)

buddy.age = 10
print(buddy.age)

miles.species = "Felis silvestris"
print(miles.species)


# print(miles.description())
print(miles.speak("Woof Woof!"))

names = ["Miles", "Buddy", "Jack"]
print(miles)