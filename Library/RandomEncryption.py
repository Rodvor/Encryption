import os
import random

def MakeLibrary():
	
	if os.path.exists("Decrypted.txt"):
		os.remove("Decrypted.txt")
	
	if os.path.exists("Encrypted.txt"):
		os.remove("Encrypted.txt")
	
	file = open(f"Preset/Decrypted.txt","r")
	characters = file.read()
	file.close()
	
	file = open(f"Decrypted.txt","w")
	file.write(characters)
	file.close()
	
	characterAmount = len(characters)
	Library = ""
	while characterAmount != 0:
		
		
		selectCharacter = random.randint(0, characterAmount - 1)
	
		
		letter = characters[selectCharacter]
		Library = Library + letter
		characters = characters.replace(letter, "")
		characterAmount = characterAmount - 1
	
	print("Library complete\n")
	print(Library)
	
	file = open("Encrypted.txt","w")
	file.write(Library)
	file.close()
	
	input()

MakeLibrary()