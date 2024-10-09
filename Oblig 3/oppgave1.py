#opretter info om studenten
student = { 
    "first name" : "Ola", 
    "last name" : "Nordmann",
    "favourite course" : "Programmering 1" 
} 


#printer ut first name og last name
print(f"studenten heter: {student['first name']} {student["last name"]}")


#legger til fagkode til programmering 1 og printer ut
student["favourite course"] = "ITF10219 "+student["favourite course"]
print(student["favourite course"])


#legger til alderen til Ola og skriver den ut
student ["age"] = 32
print(f"ola er {student['age']} år gammel")