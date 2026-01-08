class ShipCharSheet:
	CONST_ACCELERATION_TO_MASS_RATIO_SIGMOID_SCALE_VALUE = 0.5
	CONST_ACCELERATION_TO_MASS_RATIO_ABSOLUTE_LIMIT = 10

	def __init__(self):
		pass

	def GetShieldTotalHitPoints() -> float:
		pass

	def GetShieldCurrentHitPoints() -> float:
		pass

	def GetShieldDowntime() -> int:
		pass

	def GetShieldRegeneration() -> float:
		pass

	def GetShieldPowerEfficiency() -> float:
		pass

	def GetArmorTotalHitPoints() -> float:
		pass

	def GetArmorCurrentHitPoints() -> float:
		pass

	def GetHullTotalHitPoints() -> float:
		pass

	def GetHullCurrentHitPoints() -> float:
		pass

	def GetHeatAccumulationRate() -> float:
		pass

	def GetHeatLowDissipationRate() -> float:
		pass

	def GetHeatHighDissipationRate() -> float:
		pass

	def GetAccelerationPower() -> float:
		pass

	def GetDefaultMass() -> float: # the mass that comes with the ship itself
		pass

	def GetTotalMass() -> float:
		pass

	def GetAccelerationToMassRatio() -> float: 
		pass

	def GetDodgeChance() -> float:
		pass

	def GetCommandControlSpeed() -> float:
		pass

	def GetTotalTargets() -> float:
		pass