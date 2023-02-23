import math

def encrypt(plainText, a, b):
	plainText = plainText.lower()
	cipherText = ""
	for letter in plainText:
		if letter == " ": cipherText += " "
		else: cipherText += chr((a * (ord(letter) - 97) + b) % 26 + 97)
	return cipherText

def decrypt(cipherText, a, b):
	a_inverse = pow(a, -1, 26)
	plainText = ""
	for letter in cipherText:
		if letter == " ": plainText += " "
		else: plainText += chr(a_inverse * (ord(letter) - 97 - b) % 26 + 97)
	return plainText

def main():
	a = int(input("Enter the value of 'a': "))
	b = int(input("Enter the value of 'b': "))
	if math.gcd(a, 26) != 1: 
		print("'a' should be a coprime of 26")
		return
	inputText = input("Enter the text you want to encrypt: ")
	cipherText = encrypt(inputText, a, b)
	print("Encrypted Text: " + cipherText)
	plainText = decrypt(cipherText, a, b)
	print("Decrypted Text: " + plainText)

if __name__ == "__main__":
	main()