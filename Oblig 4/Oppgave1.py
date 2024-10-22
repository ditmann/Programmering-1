
#klassen min som lager objekter av filmene
class film:
        def __init__(self, name, year, score,):
            self.name = name
            self.year = year
            self.score = score

#Metode som skriver ut filmer laget av klassen
        def print_film(self):
              print(f"{self.name} was released in {self.year} and has currently a score of {self.score}")




#lager objekter ved hjelp av klassen min
film1 = film("inception",2010,0.8,)
film2 = film("The Martian",2015,8.0,)
film3 = film("Joker",2019,8.4,)

#printer alle filmene
film1.print_film()
film2.print_film()
film3.print_film()