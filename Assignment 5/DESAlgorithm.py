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

number_of_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

all_subkeys = []

def convert_hex_to_binary(hex_string):
	binary_string = ""
	for hex_char in hex_string:
		binary_string += hex_to_binary_mapping[hex_char]
	return binary_string

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

def get_plain_text_after_initial_permutation(plain_text):
	plain_text_after_initial_permutation = ""
	for index in range(len(initial_permutation)):
		plain_text_after_initial_permutation += plain_text[initial_permutation[index] - 1]
	return plain_text_after_initial_permutation

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
	all_splits = []
	split = ""
	for index in range(len(right)):
		if index % 6 == 0 and index != 0:
			all_splits.append(split)
			split = ""
		else: split += right[index]
	all_splits.append(split)

	right_after_compression = ""
	for index in range(len(all_splits)):
		row = int(all_splits[index][0] + all_splits[index][-1], 2)
		col = int(all_splits[index][1:-1], 2)
		right_after_compression += integer_to_binary_mapping[all_s_boxes[index][row][col]]
	return right_after_compression

def implement_des_algorithm():
	plain_text = input("Enter the plain text: ")
	key = input("Enter the key: ")
	print(plain_text)
	print(key)
	plain_text_binary = convert_hex_to_binary(plain_text)
	key_binary = convert_hex_to_binary(key)
	print(plain_text_binary)
	print(key_binary)
	generate_all_subkeys(key_binary)
	print(all_subkeys)
	plain_text_after_initial_permutation = get_plain_text_after_initial_permutation(plain_text_binary)
	print(plain_text_after_initial_permutation)
	left = plain_text_after_initial_permutation[:len(plain_text_after_initial_permutation) // 2]
	right = plain_text_after_initial_permutation[len(plain_text_after_initial_permutation) // 2:]
	print(left)
	print(right)

	for round_index in range(16):
		right_after_expansion = get_right_after_expansion(right)
		right_after_xor = get_result_after_xor(right_after_expansion, all_subkeys[round_index])
		right_after_compression = get_right_after_compression(right_after_xor)
		right_after_xor = get_result_after_xor(left, right_after_compression)
		
		left = right
		right = right_after_xor
		print(left, right)

if __name__ == "__main__":
	implement_des_algorithm()