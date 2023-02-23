import math

def encrypt(alphabet, plainText, a, b):
	cipherText = ""
	for letter in plainText:
		if letter == " ": cipherText += " "
		else: 
			letterIndex = alphabet.index(letter)
			cipherIndex = (a * letterIndex + b) % len(alphabet)
			cipherText += alphabet[cipherIndex]
	return cipherText

def decrypt(alphabet, cipherText, a, b):
	a_inverse = pow(a, -1, 26)
	plainText = ""
	for letter in cipherText:
		if letter == " ": plainText += " "
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
	alphabet = getAlphabetFromFile("input.txt")
	a = int(input("Enter the value of 'a': "))
	b = int(input("Enter the value of 'b': "))
	if math.gcd(a, 26) != 1: 
		print("'a' should be a coprime of 26")
		return
	inputText = input("Enter the text you want to encrypt: ")
	inputText = inputText.lower()
	cipherText = encrypt(alphabet, inputText, a, b)
	print("Encrypted Text: " + cipherText)
	plainText = decrypt(alphabet, cipherText, a, b)
	print("Decrypted Text: " + plainText)

if __name__ == "__main__":
	main()