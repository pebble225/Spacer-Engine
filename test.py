def setup(gint: "gameInstance"):
	gint.a = 1


class gameInstance:
	def __init__(self):
		self.a = None
	
	def main(self):
		setup(self)

		print(self.a)

g = gameInstance()
g.main()
