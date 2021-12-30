from pyfiglet import figlet_format
from termcolor import colored
import random
colors = ['red', 'green', 'blue', 'magenta', 'cyan', 'white']
message = input("What message do you want to print? ")
color = input("What color? ")
if color not in colors:
	color = random.choice(colors)
art = figlet_format(message)
colored_art = colored(art, color = color)
print(colored_art)
