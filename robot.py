from time import sleep

class Robot:

	def __init__(self, name='Spot', battery=100, skills=[]):
		self.name = name
		self.battery = battery
		self.skills = skills

	def charge(self):
		self.battery = 100
		print("Charging")
		# sleep(5)
		print(f"I am {self.battery}% charged.")

	def say_name(self):
		if self.battery > 0:
			self.battery-=1
			print(f"BEEP BOOP BEEP BOOP. I am {self.name.upper()}. My battery is {self.battery}%.")
		else:
			print("Low power. Please charge and try again")

	def learn_skill(self):
		
		cost_to_learn = 10
		if self.battery >= cost_to_learn:
			new_skill = input("Enter skill name: ")
			self.battery-=cost_to_learn
			self.skills.append(new_skill)
			print(f"WOAH. I KNOW {new_skill.upper()}. My battery is {self.battery}%.")
		else:
			print("Insufficient battery. Please charge and try again.")


	def menu(self):
		print("[1] Charge me!")
		print("[2] What's your name?")
		print("[3] Let's learn something new!")
		print("[4] Shut down")

if __name__ == "__main__":
	robot = Robot()
	robot.menu()
	option = int(input("Choose an option: "))

	while option != 4:
		if option == 1:
			robot.charge()
		elif option == 2:
			robot.say_name()
		elif option == 3:
			robot.learn_skill()
		else:
			print("Invalid option! Please try again.")

		# sleep(2)
		print()
		robot.menu()
		option = int(input("Choose an option: "))

