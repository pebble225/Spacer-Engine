from enum import Enum, auto

class colors(Enum):
	RED = auto()
	YELLOW = auto()
	GREEN = auto()
	BLUE = auto()


def main():
	print(colors.BLUE > colors.RED)


if __name__ == "__main__":
	main()