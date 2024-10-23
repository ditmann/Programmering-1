#lager kort og legger i liste

hjerte = "\u2665"
kløver = "\u2663"
ruter = "\u2666"
spar = "\u2660"
number = 5


hor_line = '\u2500'
vert_line = '\u2502'
bot_l_corner = '\u2514'
top_l_corner = '\u250C'
bot_r_corner = '\u2518'
top_r_corner = '\u2510'

card = f"""{top_l_corner + hor_line + hor_line + hor_line + hor_line + top_r_corner + "\n"} 
{+ vert_line + number + hjerte + vert_line}



test """ 
print(card)



print("\u2665")
print("\u2663")
print("\u2666")
print("\u2660")

print("""
-----
| \u2665 |
| 5 |
-----         
""")
