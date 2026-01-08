import math

from spacerEngine.menus.menuNode import MenuNode
from spacerEngine.menus.describableMenu import DescribableMenu
from spacerEngine.menus.simpleMenu import SimpleMenu

from spacerEngine.gameContent import GameContent

class GameInstance:
	def __init__(self):
		self.running = True

		self.startMenu = None

	def main(self):
		GameContent.Setup(self)


def customSigmoid(x: float, modifier: float):
	return 1.0 / (1.0 + math.pow(2.71828, -1*modifier/x))