
#selve klassen 
class Student:
    def __init__ (self,firstName,lastName,age,studentId,):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.studentId = studentId

    def getFullName(self):
        return f"{self.firstName} {self.lastName}"

#lager ett objekt NilsNilsen med klassen
nilsNilsen = Student("Nils","Nilsen",22,"IT567")
anneAnnesen = Student("Anne","Annesen",23,"IT012")

print(f"{nilsNilsen.firstName} er {nilsNilsen.lastName} er {nilsNilsen.age} år gammel.")
print(f"{anneAnnesen.firstName} er {anneAnnesen.lastName} er {anneAnnesen.age} år gammel.")

print(nilsNilsen.getFullName())
print(anneAnnesen.getFullName())