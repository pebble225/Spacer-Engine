from spacerEngine.menus import MenuNode
from spacerEngine.menus import DescribableMenu

from spacerEngine.ConsoleClear import clear

class SimpleMenu(DescribableMenu):
	def __init__(self):
		super().__init__()
		self.onLocationDescription = None
	
	def AddOnLocationDescription(self, onLocationDescription):
		self.onLocationDescription = onLocationDescription
	
	def GetOnLocationDescription(self) -> str:
		return self.onLocationDescription

	def VaidateOnLocationDescription(self):
		if self.onLocationDescription is None:
			raise ValueError("Location description needs to be initialized. Object {self}")
	
	def AddTravelLocation(self, menu: MenuNode):
		self.Navigation_Insert("travel", menu)

	def run(self) -> MenuNode:
		

		running = True

		nextMenu = self

		while running:
			clear()
			print(self.onLocationDescription)
			print("Enter a location number from below.\n")
			entryList = self.Navigation_SelectAllWhereType("travel")

			i = 1
			for entry in entryList:
				if not isinstance(entry["menu"], DescribableMenu):
					raise TypeError("Simple Menu is only designed to work with other describable menus.")
				print(f"({i}) {entry["menu"].description}")
				i += 1
			
			com = input("> ")
			try:
				com = int(com)

				if com > 0 and com < len(entryList)+1:
					nextMenu = entryList[com - 1]["menu"]
			except ValueError:
				pass

		
		return nextMenu