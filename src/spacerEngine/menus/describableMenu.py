from spacerEngine.menus.menuNode import MenuNode

class DescribableMenu(MenuNode):
    """
	This menu with a description that other menus can use to describe it.
	"""

    def __init__(self):
        super().__init__()

        self.travelDescription = None

    def AddTravelDescription(self, travelDescription: str):
        self.travelDescription = travelDescription

    def GetTravelDescription(self) -> str:
        return self.travelDescription

    def ValidateTravelDescription(self):
        if self.travelDescription is None:
            raise ValueError("Travel description needs to be initialized. Object {self}")