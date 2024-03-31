class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.breed = breed

    
    # def description(self):
    #     return f"{self.name} is {self.age} years old"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        # return f"{self.name} says {self.sound}"
        # there is no self sound - we access this parameter directly from a function
        return f"{self.name} barks: {sound}"
        

# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")


# buddy.age = 10
# print(buddy.age)

# miles.species = "Felis silvestris"
# print(miles.species)


# print(miles.description())
# print(miles.speak("Woof Woof!"))
# print(buddy.speak("Yap"))
# print(jim.speak("Woof"))
# print(jack.speak("Woof"))

# names = ["Miles", "Buddy", "Jack"]
# print(miles)

class JackRussellTerrier(Dog):
    def speak(self, sound = "Arf"):
        # return f"{self.name} says {sound}" 
        # not to lose changes made in parent:
        return super().speak(sound) #find speak method in Dog and call with sound variable

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

# print(miles.species)
# print(buddy.name)
# print(jack)
# print(jim.speak("Woof")) #the sound was not added, so add it here
# print(type(miles)) #to know what class object belongs to
# print(isinstance(miles, Dog))
# print(isinstance(miles, Bulldog))
# print(isinstance(jack, Dachshund))
print(miles.speak())
print(miles.speak("Grrr")) 
print(jim.speak("Woof")) #because we edited parent and did not override