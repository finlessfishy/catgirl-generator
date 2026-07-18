import sys
import os
import random
from pathlib import Path
from datetime import datetime
import email
from email.message import EmailMessage
import smtplib
import ssl

import cftoolbox as toolbox
import extra
from extra import colors as col

#os.system("catgirl generator")



color = ""
namecolor = ""

userinput = ""

name = ""

meowing = False
sleepy = False
screaming = False
blushing = False
sneezing = False
actions = False

result_meowing = ""
result_sleepy = ""
result_screaming = ""
result_blushing = ""
result_sneezing = ""
result_actions = ""

result = []

randomized = False

eyecolor = ""
haircolor = ""
timeofbirth = ""

interests = []

asciion = True



def setup():
	global userinput
	global asciion

	if asciion == True:
		print(f"welcome to catgirl generator {extra.ascii.CAT}")
	else:
		print(f"welcome to catgirl generator")

	print(f'\nenter "{col.GREEN}play{col.RESET}" to start the game')
	print(f'enter "{col.RED}exit{col.RESET}" to exit the game')
	print(f'\nenter "toggleascii" to toggle ASCII art on/off')

	userinput = confirm()

	def play():
		getnamecolor()

		print("\n")

		variable = getcatgirl()

		if variable != None:
			if variable == "error":
				print("error, unidentified command")

				getcatgirl()

	match userinput:
		case "play" | "y":
			play()
		case "exit" | "n":
			sys.exit()
		case "toggleascii":
			if asciion == True:
				print("ASCII art is now toggled OFF)")
				asciion = False
			else:
				print("ASCII art is now toggled ON)")
				asciion = True
		case _:
			print("error")
			sys.exit()
			return

def getnamecolor():
	global namecolor

	rng = random.randint(1, 7)

	if rng == 1:
		namecolor = col.RED
	elif rng == 2:
		namecolor = col.BLUE
	elif rng == 3:
		namecolor = col.GREEN
	elif rng == 4:
		namecolor = col.YELLOW
	elif rng == 5:
		namecolor = col.PURPLE
	elif rng == 6:
		namecolor = col.WHITE
	elif rng == 7:
		namecolor = col.CYAN

def getcatgirl():
	global userinput
	global meowing
	global sleepy
	global screaming
	global blushing
	global sneezing
	global actions
	global result_meowing
	global randomized
	randomized = True
	toolbox.clear()
	userinput = confirm(f"\ndo you want your {namecolor}catgirl{col.RESET} to be {col.YELLOW}meowing?{col.RESET} [{col.GREEN}y{col.RESET}/{col.RED}n{col.RESET}]")
	if userinput == "y":
		meowing = True
	elif userinput == "n":
		meowing = False
	else: 
		if userinput == "_random":
			print("randomizing")
			randomized = True
		else:
			print("error")
			return "error"

	if randomized == True:
		toolbox.clear()
		userinput = confirm(f"do you want your {namecolor}catgirl{col.RESET} to be {col.YELLOW}sleepy?{col.RESET} [{col.GREEN}y{col.RESET}/{col.RED}n{col.RESET}]")
		if userinput == "y":
			sleepy = True
		elif userinput == "n":
			sleepy = False
		else:
			print("error")
			return "error"

		toolbox.clear()
		userinput = confirm(f"do you want your {namecolor}catgirl{col.RESET} to be {col.YELLOW}screaming?{col.RESET} [{col.GREEN}y{col.RESET}/{col.RED}n{col.RESET}]")
		if userinput == "y":
			screaming = True
		elif userinput == "n":
			screaming = False
		else:
			print("error")
			return "error"

		toolbox.clear()
		userinput = confirm(f"do you want your {namecolor}catgirl{col.RESET} to be {col.YELLOW}blushing?{col.RESET} [{col.GREEN}y{col.RESET}/{col.RED}n{col.RESET}]")
		if userinput == "y":
			blushing = True
		elif userinput == "n":
			blushing = False
		else:
			print("error")
			return "error"

		toolbox.clear()
		userinput = confirm(f"do you want your {namecolor}catgirl{col.RESET} to be {col.YELLOW}sneezing?{col.RESET} [{col.GREEN}y{col.RESET}/{col.RED}n{col.RESET}]")

		if userinput == "y":
			sneezing = True
		elif userinput == "n":
			sneezing = False
		else:
			print("error")
			return "error"

		toolbox.clear()
		userinput = confirm(f"do you want your {namecolor}catgirl{col.RESET} to do {col.YELLOW}actions?{col.RESET} [{col.GREEN}y{col.RESET}/{col.RED}n{col.RESET}]")
		if userinput == "y":
			actions = True
		elif userinput == "n":
			actions = False
		else:
			print("error")
			return "error"

		complete()
		puttogether()
		printcatgirl()

def confirm(prompt = "catgirl generator"):
	prompt = f"{prompt} > "
	inputvar = input(prompt)

	if inputvar == "y":
		return "y"
	elif inputvar == "n":
		return "n"
	else:
		return inputvar

def meow():
	global result_meowing
	global randomized

	if randomized == True and random.randint(1, 2) == 1:
		if random.randint(1, 7) != 7:
			meowornyaa = random.randint(1, 2)

			if meowornyaa == 1:
				rng = random.randint(1, 10)
				rng2 = random.randint(1, 3)
				rng3 = random.randint(1, 2)

				o = "o" * rng
				e = "e" * rng2
				w = "w" * rng3

				result_meowing = f"m{e}{o}{w}"
			else:
				rng = random.randint(1, 10)
				rng2 = random.randint(1, 4)
				rng3 = random.randint(1, 2)
				rng4 = random.randint(1, 3)

				a = "a" * rng
				y = "y" * rng2
				n = "n" * rng3
				h = "h" * rng4

				if random.randint(1, 2) == 1:
					result_meowing = f"{n}{y}{a}"
				else:
					result_meowing = f"{n}{y}{a}{h}"
		else:
			result_meowing = "mrow"

		result.append(result_meowing)

def sleep():
	global result_sleepy
	global randomized

	if randomized == True and random.randint(1, 2) == 1:
		if random.randint(1, 7) != 7:
			if random.randint(1, 3) != 3:
				rng = random.randint (1, 2)

				if rng == 1:
					result_sleepy = f"*falls asleep*"
				elif rng == 2:
					result_sleepy = f"*starts snoring*"
			else:
				match random.randint (1, 4):
					case 1:
						result_sleepy = f"*passes out* (she's sleepy)"
					case 2:
						result_sleepy = f"*passes out* (she's eepy)"
					case 3:
						result_sleepy = f"*passes out* (she's a sleepy girl)"
					case 4:
						result_sleepy = f"*passes out* (she's an eepy girl)"
		else:
			if random.randint(1, 2) == 1:
				pass

				rng = random.randint(1, 2)
				rng2 = random.randint(1, 12)
				rng3 = random.randint(1, 4)
				rng3 = random.randint(1, 2)

				
				y = "y" * rng
				a = "a" * rng2
				w = "w" * rng3
				n = "n" * rng4

				result_sleepy = f"{y}{a}{w}{n}"
			else:
				result_sleepy = "*yawns*"

		result.append(result_sleepy)

def scream():
	global result_screaming
	global randomized

	if randomized == True and random.randint(1, 2) == 1:
		rng = random.randint(3, 23)
		rng2 = random.randint(2, 7)

		if random.randint(1, 10) >= 8:
			a = "A" * rng
			h = "H" * rng2
		else:
			a = "a" * rng
			h = "h" * rng2

		result_screaming = f"{a}{h}"

		result.append(result_screaming)

def blush():
	global result_blushing
	global randomized

	if randomized == True and random.randint(1, 2) == 1:
		if random.randint(1, 2) == 1:
			direction = random.randint(1,2)

			if direction == 1:
				rng = random.randint(3, 10)
				slashes = "/" * rng
				result_blushing = f">{slashes}<"
			else:
				rng = random.randint(3, 10)
				slashes = "\\" * rng
				result_blushing = f">{slashes}<"
		else:
			rng = random.randint(1, 2)

			if rng == 1:
				result_blushing = "*blushes*"
			elif rng == 2:
				result_blushing = "blushes cutely"

	result.append(result_blushing)

def sneeze():
	global result_sneezing
	global randomized

	if randomized == True and random.randint(1, 2) == 1:
		if random.randint(1, 15) != 15:
			match random.randint(1, 4):
				case 1:
					result_sneezing = f"*sneezes*"
				case 2:
					result_sneezing = f"*sneezes cutely*"
				case 3:
					result_sneezing = f"*achoo*"
				case 4:
					result_sneezing = f"achoo"
		else:
			rng = random.randint(1, 2)

			if rng == 1:
				result_sneezing = f"*coughs*"
			elif rng == 2:
				result_sneezing = f"*coughs cutely*"
		
		result.append(result_sneezing)

def action():
	global result_actions
	global randomized

	if randomized == True and random.randint(1, 2) == 1:
		if random.randint(1, 14) != 14:
			match random.randint(1, 18):
				case 1:
					result_actions = f"*falls*"
				case 2:
					result_actions = f"*sits on your keyboard*"
				case 3:
					result_actions = f"*purrs*"
				case 4:
					result_actions = f"*meows*"
				case 5:
					result_actions = f"*stares at you*"
				case 6:
					result_actions = f"*falls*"
				case 7:
					result_actions = f"*randomly jumps*"
				case 8:
					result_actions = f"*tilts head*"
				case 9:
					result_actions = f"*ear twitches*"
				case 10:
					result_actions = f"*ear twitches slightly*"
				case 11:
					result_actions = f"*tail starts wagging*"
				case 12:
					result_actions = f"*tail wags*"
				case 13:
					result_actions = f"*pounces on you*"
				case 14:
					result_actions = f"*bites you*"
				case 15:
					result_actions = f"*bites you affectionately*"
				case 16:
					result_actions = f"*snuggles you*"
				case 17:
					result_actions = f"*hugs you*"
				case 18:
					result_actions = f"*cuddles*"
		else:
			match random.randint(1, 4):
				case 1:
					result_actions = f"*starts blabbering*"
				case 2:
					result_actions = f"*starts blabbering about nothing*"
				case 3:
					result_actions = f"*starts blabbering about fish*"
				case 4:
					result_actions = f"*starts blabbering about milk*"

			result.append(result_actions)
	
def promptname():
	global userinput
	global name
	global namecolor

	toolbox.clear()
	userinput = input(f"name your {namecolor}catgirl{col.RESET}: {namecolor}")

	if userinput != "_random":
		toolbox.clear()
		print(f'{col.RESET}you chose {namecolor}{userinput}{col.RESET}')

		confirmvar = confirm(f"are you sure? [{col.GREEN}y{col.RESET}/{col.RED}n{col.RESET}] ")

		if confirmvar != None:
			if confirmvar == "y":
				name = userinput
			elif confirmvar == "n":

				promptname()
	else:
		names = []

		names = [
			"kitty",
			"meow",
			"cat",
			"catgirl",
			"Kurt Cobain",
			"mommy neko",
			"skull crusher",
			"fishstick",
			"col.WHITE fluffy",
			"pecky"
		]

		length = len(names)

		rng = random.randint(1, length)

		randname = names[rng]

		name = randname



def complete():
	global userinput
	global meowing
	global sleepy
	global screaming
	global blushing
	global sneezing
	global actions

	randomstuff()

	if meowing == True:
		meow()
		if random.randint(1, 3) == 3:
			meow()
			if random.randint(1, 2) == 2:
				meow()
				if random.randint(1, 5) == 5:
					meow()
	if sleepy == True:
		sleep()
		if random.randint(1, 4) == 4:
			sleep()
			if random.randint(1, 3) == 3:
				sleep()
	if screaming == True:
		scream()
		if random.randint(1, 4) == 4:
			scream()
			if random.randint(1, 3) == 3:
				scream()
	if blushing == True:
		blush()
		if random.randint(1, 4) == 4:
			blush()
			if random.randint(1, 3) == 3:
				blush()
	if sneezing == True:
		sneeze()
		if random.randint(1, 4) == 4:
			sneeze()
			if random.randint(1, 3) == 3:
				sneeze()
	if actions == True:
		action()
		if random.randint(1, 4) == 4:
			action()
			if random.randint(1, 3) == 3:
				action()

	promptname()

def randomstuff():
	global result

	if random.randint(1, 4) == 4:
		result.append(":3")
	if random.randint(1, 4) == 4:
		result.append(":3")
	if random.randint(1, 4) == 4:
		result.append(":3")
	if random.randint(1, 4) == 4:
		result.append("*hisses*")
	if random.randint(1, 5) == 5:
		result.append(":p")
	if random.randint(1, 7) == 7:
		result.append("(˶˃ ᵕ ˂˶)")
	if random.randint(1, 7) == 7:
		result.append("(˶ˆᗜˆ˵)")
	if random.randint(1, 7) == 7:
		result.append(">⩊<")
	if random.randint(1, 7) == 7:
		result.append("(˶>⩊<˶)")
	if random.randint(1, 10) == 10:
		result.append("(,,>﹏<,,)")

def puttogether():
	global result_meowing
	global result_sleepy
	global result_screaming
	global result_blushing
	global result_sneezing
	global result_actions
	global result

	random.shuffle(result)

	separator = ' '
	result = separator.join(result)

def printcatgirl():
	global userinput
	global result
	global name
	global asciion

	toolbox.clear()

	print(f"\n{namecolor}{name}{col.RESET}:")
	print(f"\n {col.PINK}{result}{col.RESET}")

	if asciion == True:
		print(extra.ascii.CATGIRL)

	print(f'\nenter "save" to save {namecolor}{name}{col.RESET} as a text file and see some extra info about her')

	userinput = confirm()

	if userinput == "save":
		save()

def geteyecolor():
	global eyecolor

	match random.randint(1, 12):
		case 1:
			eyecolor = "col.BLUE"
		case 2:
			eyecolor = "col.GREEN"
		case 3:
			eyecolor = "brown"
		case 4:
			eyecolor = "hazel"
		case 5:
			eyecolor = "gray"
		case 6:
			eyecolor = "col.YELLOW"
		case 7:
			eyecolor = "col.RED"
		case 8:
			eyecolor = "col.PINK"
		case 9:
			eyecolor = "col.PURPLE"
		case 10:
			eyecolor = "black"
		case 11:
			eyecolor = "golden"
		case 12:
			eyecolor = "heterochromia"
	
def gethaircolor():
	global haircolor

	if random.randint(1, 30) != 30:
		match random.randint(1, 8):
			case 1:
				haircolor = "blond"
			case 2:
				haircolor = "brunette"
			case 3:
				haircolor = "black"
			case 4:
				haircolor = "col.PINK"
			case 5:
				haircolor = "col.RED"
			case 6:
				haircolor = "col.BLUE"
			case 7:
				haircolor = "col.PURPLE"
			case 8:
				haircolor = "col.GREEN"
	else:
		haircolor = "bald"
	
def getinterests():
	global interests

	rng = random.randint(1, 16)

	if rng == 1:
		if "video games" not in interests:
			interests.append("video games")
		else:
			getinterests()
	elif rng == 2:
		if "reading" not in interests:
			interests.append("reading")
		else:
			getinterests()
	elif rng == 3:
		if "movies" not in interests:
			interests.append("movies")
		else:
			getinterests()
	elif rng == 4:
		if "cats" not in interests:
			interests.append("cats")
		else:
			getinterests()
	elif rng == 5:
		if "anime" not in interests:
			interests.append("anime")
		else:
			getinterests()
	elif rng == 6:
		if "drawing" not in interests:
			interests.append("drawing")
		else:
			getinterests()
	elif rng == 7:
		if "comics" not in interests:
			interests.append("comics")
		else:
			getinterests()
	elif rng == 8:
		if "programming" not in interests:
			interests.append("programming")
		else:
			getinterests()
	elif rng == 9:
		if "music" not in interests:
			interests.append("music")
		else:
			getinterests()
	elif rng == 10:
		if "sleeping" not in interests:
			interests.append("sleeping")
		else:
			getinterests()
	elif rng == 11:
		if "writing" not in interests:
			interests.append("writing")
		else:
			getinterests()
	elif rng == 11:
		if "painting" not in interests:
			interests.append("painting")
		else:
			getinterests()
	elif rng == 12:
		if "meowing" not in interests:
			interests.append("meowing")
		else:
			getinterests()
	elif rng == 13:
		if "hissing" not in interests:
			interests.append("hissing")
		else:
			getinterests()
	elif rng == 14:
		if "making biscuits" not in interests:
			interests.append("making biscuits")
		else:
			getinterests()
	elif rng == 15:
		if "cooking" not in interests:
			interests.append("cooking")
		else:
			getinterests()
	elif rng == 16:
		if "baking" not in interests:
			interests.append("baking")
		else:
			getinterests()
	elif rng == 17:
		if "nature" not in interests:
			interests.append("nature")
		else:
			getinterests()
	elif rng == 18:
		if "dogs" not in interests:
			interests.append("dogs")
		else:
			getinterests()
	elif rng == 19:
		if "humans" not in interests:
			interests.append("humans")
		else:
			getinterests()
	elif rng == 20:
		if "yuri" not in interests:
			interests.append("yuri")
		else:
			getinterests()
	
def save():
	global result
	global name
	global interests

	file = open(f"{name}.txt", "x")

	os.makedirs("catgirls", exist_ok=True)

	with open(f"catgirls/{name}.txt", "w") as file:
		geteyecolor()
		gethaircolor()

		for x in range(3):
			getinterests()

			if random.randint(1, 7) == 7:
				getinterests()

		global namecolor

		random.shuffle(interests)

		separator = ', '
		interests = separator.join(interests)

		if namecolor == col.RED:
			namecolor = "col.RED"
		elif namecolor == col.BLUE:
			namecolor = "col.BLUE"
		elif namecolor == col.GREEN:
			namecolor = "col.GREEN"
		elif namecolor == col.YELLOW:
			namecolor = "col.YELLOW"

		file.write(
			f"statement:\n\n{result}\n\n\nname: {name}\neye color: {eyecolor}\nhair color: {haircolor}\nname color: {namecolor}\n\ninterests: {interests}\n\n\ntime of creation: {timeofbirth}\n\nmeowing: {meowing}\nsleepy: {sleepy}\nscreaming: {screaming}\nblushing: {blushing}\nsneezing: {sneezing}\nactions: {actions}\n\nstatement length: {len(result)}")

		os.remove(f"{name}.txt")

		print(f'{col.BLUE}{name}{col.RESET} has been saved as "{col.BLUE}{name}{col.RESET}.txt"')

def gettime():
	global timeofbirth

	timeofbirth = datetime.now()


if __name__ == "__main__":
	toolbox.clear()
	setup()