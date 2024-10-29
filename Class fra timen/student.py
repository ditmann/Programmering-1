
#selve klassen 
class Student:
    def __init__ (self, firstName, lastName, age, studentId, ):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.studentId = studentId
        self.courses = []

    def getFullName(self):
        return f"{self.firstName} {self.lastName}"
    
    def enrollInCourse(self,Course):
        self.courses.append(Course)

    def getTotalCredits(self):
        total_credits = 0
        for course in self.courses:
            total_credits += course.credits
        return total_credits 


class Course:
    def __init__(self, name, code, credits, ):
        self.name = name
        self.code = code
        self.credits = credits
