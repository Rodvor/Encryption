def Decryption(string): #Encrypted String -> string
	
	file = open("Library/decrypted.txt","r") #Retrieves a string of letters, which are in order: abcdefg...
	DC = file.read()
	file.close()
	
	file = open("Library/encrypted.txt","r") #Retrieves a string of letters, which are in random order: the encryption key
	EC = file.read()
	file.close()
	
	stringLength = len(string) #Length of the string
	length = len(EC) #Number of characters in the key
	index = 0 #Sets index to 0, in order to start from the first character
	decryptedString = ""
	addition = 0

	while index != stringLength: #Will repeat until entire string is handeled

		stringLetter = string[index] #Takes the index letter

		spot = EC.index(stringLetter) #Finds the index of the letter in the key

		decryptedLetter = DC[(spot + addition) % length] #Finds the letter in the order that corresponds to the index of the letter in the key. Reverses encryption

		index = index + 1 #Continues to the next letter
		addition = addition - 1 #Allows reversing the encryption

		decryptedString = decryptedString + decryptedLetter #Adds the decrypted letter to the string
	
	return(decryptedString) #Returns the decrypted string 
	

print("\nString Decryption")
print("-----------------")
print(Decryption(input("Text:")))
