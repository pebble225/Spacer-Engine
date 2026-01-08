














# ENGINE PART SCAMMER MISSION

SamRockwell_TuringStation_SellingEngine = StationNode()
TuringStation.AttachStationNode(STATIONNODETYPE_NPC, SamRockwell_TuringStation_SellingEngine)
SamRockwell_TuringStation_SellingEngine.SetSpawnEvent(GAME_STARTED)
SamRockwell_TuringStation_SellingEngine.SetOnActionSpeak(EVENT_SamRockwell_TuringStation_Dialogue)

def EVENT_SamRockwell_TuringStation_Dialogue():
	menuID = "START"
	running = True

	while running:
		if menuID == "START":
			dialogue = DialoguePopup()
			dialogue.SetProfile(DialogueProfile.BUSINESSMAN_1)
			dialogue.SetText("Hey there, sport. Want to buy this high quality engine part for 500 units? It maxes out at 100 mph with efficient fuel economy.")
			dialogue.AddOption("ACCEPT", "Sure! I'll take you up on that offer.")
			dialogue.AddOption("REJECT", "No thank you.")
			
			com = dialogue.execute()

			if com == "ACCEPT" and playerInstance.inventory.credits >= 500:
				menuID = "SUCCESSFUL PURCHASE"
			elif com == "ACCEPT":
				menuID = "UNSUCCESSFUL PURCHASE"
		elif menuID == "SUCCESSFUL PURCHASE":
			dialogue = DialoguePopup()
			dialogue.SetProfile(DialogueProfile.BUSINESSMAN_1)
			dialogue.SetText("Heh heh. Enjoy your fancy new engine. Heheh")
			dialogue.AddOption("CONTINUE", "Uh okay...")

			com = dialogue.execute()

			if com == "CONTINUE":
				running = False

				TuringStation.RemoveStationNode(SamRockwell_TuringStation_SellingEngine)

