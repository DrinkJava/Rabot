import random


CURSES = ["Fuck", "Shit", "God Damnit", "Motherfucker", "Damn", "Bitch", "Crap",\
          "Piss", "Dick", "Cock", "Pussy", "Asshole", "Fag", "Nigger", "Bastard",\
          "Slut", "Douche", "Cumbumpster", "virgin"]
def curse(body):
	curse=  random.choice(CURSES)
	if curse =="Nigger":
		curse = random.choice(CURSES)
	return curse
