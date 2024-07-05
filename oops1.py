class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("sor far", self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
print(dir(an)) #list of available methods

class Animals:
    x = 1

    def __init__(self):
        print('I am Constructed')

    def party(self):
        self.x = self.x + 1
        print("sor far", self.x)
    
    def __del__(self):
        print("i am destructed", self.x)

instance1 = Animals()
instance1.party()
instance1.party()
instance1 = 42
print(instance1)    
