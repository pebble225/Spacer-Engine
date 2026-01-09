
from spacerEngine.menus.menuNode import MenuNode
from spacerEngine.menus.describableMenu import DescribableMenu
from spacerEngine.menus.simpleMenu import SimpleMenu


class GameContent:
	def Setup() -> "MenuNode":

		# predefine other

		WARPINGMODE = SimpleMenu()

		# predefine stations

		FLIGHTZONE_PEBBLESTATION = SimpleMenu()
		FLIGHTZONE_SOYUZSTATION = SimpleMenu()

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

		return FLIGHTZONE_PEBBLESTATION