import random as random

class Product:
    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = .5
        self.identifier = random.randint(1000000, 9999999)
    def stealability(self):
        if self.price / self.weight < .5:
            print("Not so stealable")
        elif .5 <= self.price / self.weight < 1:
            print("Kinda stealable")
        else:
            print("Very stealable")
    def explode(self):
        if self.flammability * self.weight < 10:
            print("...fizzle.")
        elif 10 <= self.flammability * self.weight < 50:
            print("...boom!")
        else:
            print("...BABOOM!!")

class BoxingGlove(Product):
    def __init__(self, name):
        super().__init__(name)
        self.weight = 10
    def explode(self):
        print("...it's a glove.")
    def punch(self):
        if self.weight < 5:
            print('That tickles.')
        elif 5 <= self.weight < 15:
            print('Hey that hurt!')
        else:
            print("OUCH!")