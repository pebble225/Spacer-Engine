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