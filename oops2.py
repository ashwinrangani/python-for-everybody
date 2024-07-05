class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = PartyAnimal('Sally')
s.party()

j = PartyAnimal("Jim")
j.party()


#inheritance => create subclasses from parent class, i.e extending the main class

class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

a = FootballFan('Chuck')
a.party()
a.touchdown()

#Definitions

# Class - a template
# Attribute - A variable within a class
# Method - A function within a class
# Object - A particular instance of a class
# Contructor - Code that runs when an object is created
# Inheritance - The ability to extend a class to a new class