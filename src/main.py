import os
import platform


def clear():
	osName = platform.system()

	def slowClear():
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

	if osName == "Linux" or osName == "Darwin":
		if os.system("clear") != 0:
			slowClear()
	elif osName == "Windows":
		if os.system("cls") != 0:
			slowClear()
	else:
		slowClear()

class MenuNode:
	def __init__(self):
		self.navigation = []
		self.interaction = []
	
	def Navigation_Insert(self, trigger, menu: "MenuNode"):
		self.navigation.append({"trigger": trigger, "menu": menu})
	
	def Navigation_SelectAllWhereType(self, trigger) -> list:
		return [i for i in self.navigation if i["trigger"] == trigger]
	
	def Navigation_DeleteAllWhereMenu(self, menu: "MenuNode") -> None:
		self.navigation = [i for i in self.navigation if i["menu"] != menu]

	def run(self) -> "MenuNode":
		raise NotImplementedError

class DescribableMenu(MenuNode):
	"""
	This menu with a description that other menus can use to describe it.

	Args:
		description (str): The description used by other menus.
	"""
	def __init__(self):
		super().__init__()

		self.travelDescription = None
	
	def AddTravelDescription(self, travelDescription: str):
		self.travelDescription = travelDescription
	
	def GetTravelDescription(self) -> str:
		return self.travelDescription

	def VaidateTravelDescription(self):
		if self.travelDescription is None:
			raise ValueError("Travel description needs to be initialized. Object {self}")

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

class GameContent:
	def Setup(game: "GameInstance"):

		# predefine other

		WARPINGMODE = SimpleMenu()

		# predefine stations

		FLIGHTZONE_PEBBLESTATION = SimpleMenu()
		FLIGHTZONE_SOYUZSTATION = SimpleMenu()

		# set entry point

		game.startMenu = FLIGHTZONE_PEBBLESTATION

		# warping mode

		WARPINGMODE.AddTravelDescription("Enter warp mode.")
		WARPINGMODE.AddOnLocationDescription("You are in warp mode.")
		WARPINGMODE.AddTravelLocation(FLIGHTZONE_SOYUZSTATION)
		WARPINGMODE.AddTravelLocation(FLIGHTZONE_PEBBLESTATION)

		# in orbit of pebble station

		FLIGHTZONE_PEBBLESTATION.AddTravelDescription("Orbit of pebble station.")
		FLIGHTZONE_PEBBLESTATION.AddOnLocationDescription("You are in orbit of pebble station.")
		FLIGHTZONE_PEBBLESTATION.AddTravelLocation(WARPINGMODE)

		# in orbit of soyuz station

		FLIGHTZONE_SOYUZSTATION.AddTravelDescription("Orbit of soyuz station.")
		FLIGHTZONE_SOYUZSTATION.AddOnLocationDescription("You are in orbit of soyuz station.")
		FLIGHTZONE_SOYUZSTATION.AddTravelLocation(WARPINGMODE)

class GameInstance:
	def __init__(self):
		self.running = True

		self.startMenu = None

	def main(self):
		GameContent.Setup(self)

if __name__ == "__main__":
	gameInstance = GameInstance()
	gameInstance.main()