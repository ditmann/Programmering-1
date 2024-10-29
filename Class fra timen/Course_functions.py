
#funkjson som henter ting fra klasser

def calculateTotalCredits(kurs):
    totalCredits = 0
    for object in kurs:
        totalCredits += object.credits
    return totalCredits
