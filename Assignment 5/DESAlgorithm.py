hex_to_binary_mapping = {
							"0": "0000",
							"1": "0001",
							"2": "0010",
							"3": "0011",
							"4": "0100",
							"5": "0101",
							"6": "0110",
							"7": "0111",
							"8": "1000",
							"9": "1001",
							"A": "1010",
							"B": "1011",
							"C": "1100",
							"D": "1101",
							"E": "1110",
							"F": "1111"	
						}

integer_to_binary_mapping = {
								0: "0000",
								1: "0001",
								2: "0010",
								3: "0011",
								4: "0100",
								5: "0101",
								6: "0110",
								7: "0111",
								8: "1000",
								9: "1001",
								10: "1010",
								11: "1011",
								12: "1100",
								13: "1101",
								14: "1110",
								15: "1111"
							}

binary_to_hex_mapping = {
							"0000": "0",
							"0001": "1",
							"0010": "2",
							"0011": "3",
							"0100": "4",
							"0101": "5",
							"0110": "6",
							"0111": "7",
							"1000": "8",
							"1001": "9",
							"1010": "A",
							"1011": "B",
							"1100": "C",
							"1101": "D",
							"1110": "E",
							"1111": "F"
						}

first_permutation_order = 	[57, 49, 41, 33, 25, 17, 9,
							 1, 58, 50, 42, 34, 26, 18,
							 10, 2, 59, 51, 43, 35, 27,
							 19, 11, 3, 60, 52, 44, 36,
							 63, 55, 47, 39, 31, 23, 15,
							 7, 62, 54, 46, 38, 30, 22,
							 14, 6, 61, 53, 45, 37, 29,
							 21, 13, 5, 28, 20, 12, 4]

second_permutation_order =	[14, 17, 11, 24, 1, 5,
							 3, 28, 15, 6, 21, 10,
							 23, 19, 12, 4, 26, 8,
							 16, 7, 27, 20, 13, 2,
							 41, 52, 31, 37, 47, 55,
							 30, 40, 51, 45, 33, 48,
							 44, 49, 39, 56, 34, 53,
							 46, 42, 50, 36, 29, 32]

initial_permutation = 	[58, 50, 42, 34, 26, 18, 10, 2,
						 60, 52, 44, 36, 28, 20, 12, 4,
						 62, 54, 46, 38, 30, 22, 14, 6,
						 64, 56, 48, 40, 32, 24, 16, 8,
						 57, 49, 41, 33, 25, 17, 9, 1,
						 59, 51, 43, 35, 27, 19, 11, 3,
						 61, 53, 45, 37, 29, 21, 13, 5,
						 63, 55, 47, 39, 31, 23, 15, 7]

inverse_initial_permutation = 	[40, 8, 48, 16, 56, 24, 64, 32,               
								 39, 7, 47, 15, 55, 23, 63, 31,               
								 38, 6, 46, 14, 54, 22, 62, 30,               
								 37, 5, 45, 13, 53, 21, 61, 29,               
								 36, 4, 44, 12, 52, 20, 60, 28,               
								 35, 3, 43, 11, 51, 19, 59, 27,               
								 34, 2, 42, 10, 50, 18, 58, 26,               
								 33, 1, 41, 9, 49, 17, 57, 25]

expansion_order = 	[32, 1, 2, 3, 4, 5, 4, 5,          
					 6, 7, 8, 9, 8, 9, 10, 11,          
					 12, 13, 12, 13, 14, 15, 16, 17,          
					 16, 17, 18, 19, 20, 21, 20, 21,          
					 22, 23, 24, 25, 24, 25, 26, 27,          
					 28, 29, 28, 29, 30, 31, 32, 1]

all_s_boxes = 	[[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],          
				  [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],          
				  [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],          
				  [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],           
				 [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],          
				  [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],          
				  [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],          
				  [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],           
				 [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],          
				  [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],          
				  [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],          
				  [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],           
				 [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],          
				  [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],          
				  [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],          
				  [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],           
				 [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],          
				  [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],          
				  [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],          
				  [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],           
				 [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],          
				  [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],          
				  [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],          
				  [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],           
				 [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],          
				  [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],          
				  [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],          
				  [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],           
				 [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],          
				  [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],          
				  [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],          
				  [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

right_permutation_order = 	[16,  7, 20, 21,        
							 29, 12, 28, 17,        
							 1, 15, 23, 26,        
							 5, 18, 31, 10,        
							 2,  8, 24, 14,        
							 32, 27,  3,  9,        
							 19, 13, 30,  6,        
							 22, 11,  4, 25]

number_of_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

all_subkeys = []

def convert_hex_to_binary(hex_string):
	binary_string = ""
	for hex_char in hex_string:
		binary_string += hex_to_binary_mapping[hex_char]
	return binary_string

def convert_binary_to_hex(binary_string):
	hex_string = ""
	for index in range(0, len(binary_string), 4):
		hex_string += binary_to_hex_mapping[binary_string[index: index + 4]]
	return hex_string

def get_key_after_first_perumtation_order(key):
	key_after_first_perumtation_order = ""
	for index in range(len(first_permutation_order)):
		key_after_first_perumtation_order += key[first_permutation_order[index] - 1]
	return key_after_first_perumtation_order

def get_key_after_left_shifts(key, round_index):
	return key[number_of_shifts[round_index]:] + key[:number_of_shifts[round_index]]

def get_key_after_second_perumtation_order(key):
	key_after_second_perumtation_order = ""
	for index in range(len(second_permutation_order)):
		key_after_second_perumtation_order += key[second_permutation_order[index] - 1]
	return key_after_second_perumtation_order

def generate_all_subkeys(key):
	key_after_first_perumtation_order = get_key_after_first_perumtation_order(key)
	key_left = key_after_first_perumtation_order[:len(key_after_first_perumtation_order) // 2]
	key_right = key_after_first_perumtation_order[len(key_after_first_perumtation_order) // 2:]
	for round_index in range(16):
		key_left_after_shifts = get_key_after_left_shifts(key_left, round_index)
		key_right_after_shifts = get_key_after_left_shifts(key_right, round_index)
		key_after_shifts = key_left_after_shifts + key_right_after_shifts
		key_after_second_perumtation_order = get_key_after_second_perumtation_order(key_after_shifts)
		all_subkeys.append(key_after_second_perumtation_order)
		key_left = key_left_after_shifts
		key_right = key_right_after_shifts

def get_text_after_initial_permutation(text):
	text_after_initial_permutation = ""
	for index in range(len(initial_permutation)):
		text_after_initial_permutation += text[initial_permutation[index] - 1]
	return text_after_initial_permutation

def get_right_after_expansion(right):
	right_after_expansion = ""
	for index in range(len(expansion_order)):
		right_after_expansion += right[expansion_order[index] - 1]
	return right_after_expansion

def get_result_after_xor(first, second):
	result_after_xor = ""
	for index in range(len(first)):
		if first[index] == second[index]: result_after_xor += "0"
		else: result_after_xor += "1"
	return result_after_xor 

def get_right_after_compression(right):
	right_after_compression = ""
	for index in range(8):
		row = int(right[index * 6] + right[index * 6 + 5], 2)
		col = int(right[index * 6 + 1: index * 6 + 5], 2)
		right_after_compression += integer_to_binary_mapping[all_s_boxes[index][row][col]]
	return right_after_compression

def get_right_after_permutation(right):
	right_after_permutation = ""
	for index in range(len(right_permutation_order)):
		right_after_permutation += right[right_permutation_order[index] - 1]
	return right_after_permutation

def get_text_after_inverse_initial_permutation(string):
	text_after_inverse_initial_permutation = ""
	for index in range(len(inverse_initial_permutation)):
		text_after_inverse_initial_permutation += string[inverse_initial_permutation[index] - 1]
	return text_after_inverse_initial_permutation

def implement_des_algorithm(text):
	text_after_initial_permutation = get_text_after_initial_permutation(text)
	left = text_after_initial_permutation[:len(text_after_initial_permutation) // 2]
	right = text_after_initial_permutation[len(text_after_initial_permutation) // 2:]

	for round_index in range(16):
		right_after_expansion = get_right_after_expansion(right)
		right_after_xor = get_result_after_xor(right_after_expansion, all_subkeys[round_index])
		right_after_compression = get_right_after_compression(right_after_xor)
		right_after_permutation = get_right_after_permutation(right_after_compression)
		right_after_xor = get_result_after_xor(left, right_after_permutation)
		
		left = right
		right = right_after_xor
	left, right = right, left
	cipher_text = left + right
	cipher_text = get_text_after_inverse_initial_permutation(cipher_text)
	return cipher_text

def perform_encryption():
	plain_text = input("Enter the text you want to encrypt: ")
	key = input("Enter the key you want to use: ")
	plain_text_binary = convert_hex_to_binary(plain_text)
	key_binary = convert_hex_to_binary(key)
	generate_all_subkeys(key_binary)
	cipher_text = implement_des_algorithm(plain_text_binary)
	cipher_text_hex = convert_binary_to_hex(cipher_text)
	print("Given,")
	print("\tPlain Text: ", plain_text)
	print("\tKey: ", key)
	print("The Cipher Text after performing Encryption: ", cipher_text_hex)

def perform_decryption():
	global all_subkeys
	cipher_text = input("Enter the text you want to decrypt: ")
	key = input("Enter the key you want to use: ")
	cipher_text_binary = convert_hex_to_binary(cipher_text)
	key_binary = convert_hex_to_binary(key)
	generate_all_subkeys(key_binary)
	all_subkeys = all_subkeys[::-1]
	plain_text = implement_des_algorithm(cipher_text_binary)
	plain_text_hex = convert_binary_to_hex(plain_text)
	print("Given,")
	print("\tCipher Text: ", cipher_text)
	print("\tKey: ", key)
	print("The Plain Text after performing Decryption: ", plain_text_hex)

def perform_both_encryption_and_decryption():
	global all_subkeys
	plain_text = input("Enter the text: ")
	key = input("Enter the key you want to use: ")
	plain_text_binary = convert_hex_to_binary(plain_text)
	key_binary = convert_hex_to_binary(key)
	generate_all_subkeys(key_binary)
	cipher_text = implement_des_algorithm(plain_text_binary)
	cipher_text_hex = convert_binary_to_hex(cipher_text)
	print("Given,")
	print("\tPlain Text: ", plain_text)
	print("\tKey: ", key)
	print("The Cipher Text after performing Encryption: ", cipher_text_hex)
	all_subkeys = all_subkeys[::-1]
	plain_text = implement_des_algorithm(cipher_text)
	plain_text_hex = convert_binary_to_hex(plain_text)
	print()
	print("Now,")
	print("\tCipher Text: ", cipher_text_hex)
	print("\tKey: ", key)
	print("The Plain Text after performing Decryption: ", plain_text_hex)

if __name__ == "__main__":
	print("Which Operation would you like to perform?")
	print("Enter 1 to Encrypt")
	print("Enter 2 to Decrypt")
	print("Enter 3 to do Both")
	option = int(input("Enter your option:"))

	if option == 1:
		perform_encryption()

	if option == 2:
		perform_decryption()

	if option == 3:
		perform_both_encryption_and_decryption()

