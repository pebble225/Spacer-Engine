import math

from spacerEngine.menus import *

from spacerEngine.gameContent import GameContent

class GameInstance:
	def __init__(self):
		self.running = True

		self.currentMenu = None

	def main(self):
		self.currentMenu = GameContent.Setup()

		while self.running:
			self.currentMenu = self.currentMenu.run()


def customSigmoid(x: float, modifier: float):
	return 1.0 / (1.0 + math.pow(2.71828, -1*modifier/x))