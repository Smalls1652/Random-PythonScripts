'''

mOcK-TeXT

Created by: Smalls
Website - https://smalls.online
Github - https://github.com/Smalls1652

Description:
Know that Spongebob meme where he looks like a chicken and the text is in a mocking tone? This converts text to that format.

The script is built for the iOS app Pythonista and will only work for that app; however, the main function that converts the text is mOCkTeXt() and can be utilized anywhere.

'''

import sys

#Begin Pythonista specific modules
import clipboard
import console
import appex
#End Pythonista specific modules

def textInput():
	#This function utilizes Pythonista modules.
	
	if appex.is_running_extension():
		#If arguments are not provided.	
		inputText = appex.get_text()
	else:
		#Otherwise show text input box.
		inputText = console.input_alert("mOCk TeXT", "What text would you like to mock?")
	
	if not inputText:
		console.alert("moCK TeXT", "mOCk TeXT has a null value. Exiting.", "Okay", hide_cancel_button=True)
		sys.exit()
	else:
		inputText = inputText.lower()
	
	return inputText
	
def mOCkTeXt(text):
	#This function can be utilized in any script.
	
	charUpRate = round(len(text) / (len(text) / 0.7 )) #Calculating the interval rate to capitalize letters.

	i = 0 #Interval counter
	returnText = ""

	for c in text:
		if i == charUpRate:
			#If i == charUpRate then uppercase the character and reset i back to 0
			returnText += c.upper()
			i = 0
		else:
			#Otherwise return the character as is and increment i.
			returnText += c
			i += 1
			
		return returnText
		
		
output = mOCkTeXt(textInput())
clipboard.set(output) #Set the clipboard to the return text.

console.alert("moCK TeXT", "mOCk TeXT has been copied to your clipboard.", "Okay", hide_cancel_button=True)

if appex.is_running_extension():
	appex.finish()
else:
	sys.exit()