import textwrap

def populateTextArea(strData: str, w: int, h: int):
	textAreaIndex = 0
	strDataIndex = 0

	textArea = [None] * (w * h)

	textAreaLength = w*h
	strDataLength = len(strData)

	while textAreaIndex < textAreaLength and strDataIndex < strDataLength:
		textAreaThisLine = textAreaIndex - (textAreaIndex % w)
		textAreaNextLine = textAreaThisLine + w

		# find the length of the word
		strDataWordEnd = strDataLength
		for i in range(strDataIndex, strDataLength):
			if strData[i] == " ":
				strDataWordEnd = i
				break
		
		# is this word too big for one line?

		if strDataWordEnd - strDataIndex > w:
			# fill the line and pretend the rest of the word is its own word at the start of the next line

			while textAreaIndex < textAreaNextLine and textAreaIndex < textAreaLength and strDataIndex < strDataLength:
				textArea[textAreaIndex] = strData[strDataIndex]
				textAreaIndex += 1
				strDataIndex += 1
		
		# does the word need to be wrapped to the next line?

		elif textAreaIndex + (strDataWordEnd - strDataIndex) > textAreaNextLine:
			#bump textAreaIndex to the next line and reset
			while textAreaIndex < textAreaLength and textAreaIndex < textAreaNextLine:
				textArea[textAreaIndex] = " "
				textAreaIndex += 1
		
		else:

			# Is there a free space between the current text area selection and the beginning of the line?

			foundCharacter = False

			for i in range(textAreaThisLine, textAreaIndex):
				if textArea[i] != " ":
					foundCharacter = True
			if not foundCharacter:
				# Move the index back to the start of the line.
				textAreaIndex = textAreaThisLine
			
			# populate the word on the line. No wrapping necessary

			while strDataIndex < strDataWordEnd and textAreaIndex < textAreaLength and strDataIndex < strDataLength:
				textArea[textAreaIndex] = strData[strDataIndex]
				textAreaIndex += 1
				strDataIndex += 1
			
			# scan for the next character in strData that isn't a space. Leave a space for every space.

			while textAreaIndex < textAreaLength:
				if strDataIndex < strDataLength:
					# strData won't be tested for a character if its index goes past the length
					# textArea will populate the remainder of the field with spaces and terminate
					if strData[strDataIndex] != " ":
						break
				
				textArea[textAreaIndex] = " "
				textAreaIndex += 1
				strDataIndex += 1
	
	return textArea
			
def populateTextArea2(strData: str, w: int, h: int) -> list[str]:
	wrapper = textwrap.TextWrapper(
		width=w,
		break_long_words=True,
		break_on_hyphens=False
	)

	lines = wrapper.wrap(strData)
	lines = lines[:h]
	lines = [line.ljust(w) for line in lines]

	missingLines = h - len(lines)

	lines += [" " * w] * missingLines

	return lines