from spaceRPGengine.menus.menuNode import MenuNode
from spaceRPGengine.ConsoleClear import clear

class SimpleMenu(MenuNode):
	def __init__(self, locationDescription: str):
		super().__init__()
		self.locationDescription = locationDescription
	
	def AddTravelLocation(self, menu: MenuNode):
		self.Navigation_Insert("travel", menu)

	def run(self) -> MenuNode:
		running = True
		menu = "default"

		nextMenu = self

		while running:
			if menu == "default":
				clear()
				print(self.locationDescription)
				print("type \"help\" for a list of available actions.\n")
				com = input("> ")