# setter opp hvor mange kaker hver person har med seg
Person1K = float(5)
Person2K = float(9)
Person3K = float(2.5)
person4K = float(21)
perosn5K = float(0)

#antall personer som er med
Personer = 5

#totalt hvor mange kaker som er spist
totalK = Person1K+Person2K+Person3K+person4K+perosn5K

#gjennomsnittet kaker som er spist i uka
gjennomsnitt = int(totalK/Personer) 

#skriver til terminalen hvor mange kaker som er spist i gjennomsnitt
print("gjennomsnittet av kaker som er spist iløpet av uka er %i kaker"%(gjennomsnitt))
