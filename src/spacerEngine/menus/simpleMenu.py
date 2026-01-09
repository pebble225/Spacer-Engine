from spacerEngine.menus.menuNode import MenuNode
from spacerEngine.menus.describableMenu import DescribableMenu

from spacerEngine.ConsoleClear import clear

class SimpleMenu(DescribableMenu):
    def __init__(self):
        super().__init__()
        self.onLocationDescription = None

    def AddOnLocationDescription(self, onLocationDescription):
        self.onLocationDescription = onLocationDescription

    def GetOnLocationDescription(self) -> str:
        return self.onLocationDescription

    def ValidateOnLocationDescription(self):
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
                print(f"({i}) {entry["menu"].GetTravelDescription()}")

                i += 1

            com = input("> ")
            try:
                com = int(com)

                if 1 <= com <= len(entryList):
                    nextMenu = entryList[com - 1]["menu"]
                    running = False
            except ValueError:
                pass

        return nextMenu