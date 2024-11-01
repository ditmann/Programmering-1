

class Animal:
    def __init__(self, name, age, ):
        self.name = name
        self.age = age

    def getName(self):
        return self.name



class Honeybadger (Animal):
    def __init__(self, name, age, sgiven = 0):
        super().__init__(name, age)
        self.sgiven = sgiven




nilsNilsen = Animal("Nils Nilsen", 10)
dyr1 = Honeybadger("gamer", 20, 2)

print(dyr1.getName())
print(dyr1.age)
print(dyr1.sgiven)

print(nilsNilsen.getName())