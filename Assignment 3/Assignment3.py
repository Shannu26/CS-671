import math

def encrypt(alphabet, plainText, a, b):
	cipherText = ""
	for letter in plainText:
		if letter not in alphabet: cipherText += letter
		else: 
			letterIndex = alphabet.index(letter)
			cipherIndex = (a * letterIndex + b) % len(alphabet)
			cipherText += alphabet[cipherIndex]
	return cipherText

def decrypt(alphabet, cipherText, a, b):
	a_inverse = pow(a, -1, 26)
	plainText = ""
	for letter in cipherText:
		if letter not in alphabet: plainText += letter
		else: 
			letterIndex = alphabet.index(letter)
			plainIndex = a_inverse * (letterIndex - b) % len(alphabet)
			plainText += alphabet[plainIndex]
	return plainText

def getAlphabetFromFile(filename):
	alphabet = []
	with open(filename, mode ='r') as inputFile:
		alphabet = inputFile.readline().split()
	return alphabet

def main():
	alphabet = getAlphabetFromFile("alphabet.txt")
	a = int(input("Enter the value of 'a': "))
	b = int(input("Enter the value of 'b': "))
	if math.gcd(a, len(alphabet)) != 1: 
		print("'a' should be a coprime of length of alphabet which is " + str(len(alphabet)))
		return
	print("Which operation would you like to perform?")
	operation = int(input("Enter 1 to Encrypt and 2 to Decrypt a text: "))
	if operation == 1:
		plainText = input("Enter the text you want to encrypt: ") 
		plainText = plainText.lower()
		cipherText = encrypt(alphabet, plainText, a, b)
		print("The Plain Text is: " + plainText)
		print("The Encrypted Text is: " + cipherText)
	else:
		cipherText = input("Enter the text you want to decrypt: ")
		cipherText = cipherText.lower()
		plainText = decrypt(alphabet, cipherText, a, b)
		print("The Cipher Text is: " + cipherText)
		print("The Decrypted Text is: " + plainText)

if __name__ == "__main__":
	main()