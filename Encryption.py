def Encryption(string): #String -> Encrypted string
	
	file = open("Library/decrypted.txt","r") #Retrieves a string of letters, which are in order: abcdefg...
	DC = file.read()
	file.close()
	
	file = open("Library/encrypted.txt","r") #Retrieves a string of letters, which are in random order: the encryption key
	EC = file.read()
	file.close()
	
	stringLength = len(string) #Length of the string
	length = len(EC) #Number of characters in the key
	index = 0 #Sets index to 0, in order to start from the first character
	encryptedString = "" 
	addition = 0 

	while index != stringLength: #Will repeat until entire string is handeled

		stringLetter = string[index] #Takes the index letter

		spot = DC.index(stringLetter) #Finds the index of the letter in the letters that are in order

		encryptedLetter = EC[(spot + addition) % length] #Finds the letter in the key that corresponds to the index of sorted letters. Addition makes the pattern harder and if the index is out of range, it will return back to the beginning

		index = index + 1 #Continues to the next letter
		addition = addition + 1 #Adds more to the addition

		encryptedString = encryptedString + encryptedLetter #Adds the encrypted letter to the string
	
	return(encryptedString) #Returns the encrypted string 
	

print("\nString Encryption")
print("-----------------")
print(f"Encrypted Text: {Encryption(input('Text:'))}")
