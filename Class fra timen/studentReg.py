from student import Student, Course
import Course_functions as cf

#lager kurs
Programmering1 = Course("programmering 1", "ITF 10219", 10)
webutvikling = Course("webutvikling", "ITF 18724", 10)
design = Course("design", "ITF 0783", 10)

#lager elever
nilsNilsen = Student("Nils", "Nilsen", 22, "IT678")
anneAnnesen = Student("anne", "Annesen", 23, "IT123")

#legger til i kurs
nilsNilsen.enrollInCourse(Programmering1)
nilsNilsen.enrollInCourse(webutvikling)
nilsNilsen.enrollInCourse(design)

#med klasse metode
print(nilsNilsen.getTotalCredits())

#med ekstern funksjon
print(cf.calculateTotalCredits(nilsNilsen.courses))