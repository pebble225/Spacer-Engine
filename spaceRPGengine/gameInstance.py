import math

from spaceRPGengine.enums.menuID import MenuID

class GameInstance:
	def __init__(self):
		self.running = True
		self.menu = MenuID.MAIN

	def main(self):
		com = None
		while self.running:

			if self.menu == MenuID.MAIN:
				clear()
				print(f"Star System: ")
				print(f"Site: ")
				print("\n")
				print("(1) Map")
				print("(2) ")
				print("(x) Exit")

				com = input()
				if com == "1":
					self.menu = MenuID.MAIN_MAP
				elif com == "x":
					self.running = False


def customSigmoid(x: float, modifier: float):
	return 1.0 / (1.0 + math.pow(2.71828, -1*modifier/x))