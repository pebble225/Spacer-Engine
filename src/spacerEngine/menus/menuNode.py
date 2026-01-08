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