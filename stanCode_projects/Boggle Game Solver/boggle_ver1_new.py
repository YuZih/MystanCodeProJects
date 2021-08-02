"""
File: boggle_ver1_new.py
Name: Yuzu
----------------------------------------
This program will find all the answers of boggle after user inputted 16 letters of 4 rows.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	Process:
		1. Let user input 4 rows.
		2. Read file and find possible words.
		3. Start timing after finishing filtering.
		4. Find answers of boggle and print them out.
		5. End timing and show how long it takes. (records: 0.0015 seconds)
	"""
	# let user input letters
	letters = []
	boggle = {}
	illegal_input = False
	for i in range(4):
		row = input(f'{i + 1} row of letters: ').lower().split()
		if len(row) != 4:
			print('Illegal input')
			illegal_input = True
			break
		else:
			j = 1
			for letter in row:
				if not letter.isalpha() or len(letter) != 1:
					print('Illegal input')
					illegal_input = True
					break
				else:
					if letter in boggle:
						position = boggle[letter]
						position.add((i+1, j))
						boggle[letter] = position
					else:
						position = set()
						position.add((i+1, j))
						boggle[letter] = position
					j += 1
				if illegal_input is not True:
					letters.append(letter)
			if illegal_input is True:
				break

	# Start timing after checking all rows are legal inputs.
	if illegal_input is not True:
		# pre-setting
		letters.append('\n')
		letter_type_inputted = set(letters)

		# read file and find possible words
		possible_words = set()
		with open(FILE, 'r') as f:
			for line in f:
				if line[0] in letter_type_inputted and line[1] in letter_type_inputted:
					if len(line) >= 5:
						if line[2] in letter_type_inputted and line[3] in letter_type_inputted:
							if set(line).issubset(letter_type_inputted):
								possible_words.add(line.strip())

		# find answers of boggle
		start = time.time()
		########################################################################################
		answers = 0
		for word in possible_words:
			location = 1
			path = []
			for p in boggle[word[0]]:
				path.append(p)
				if correct_word(location, word, path, boggle) is True:
					print(f'Found "{word}"')
					answers += 1
				path.pop()
		print(f'There are {answers} words in total.')
		#########################################################################################
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def correct_word(location, word, path, boggle):
	"""
	Find correct word by using recursions.
	"""
	if location == len(word):
		return True
	else:
		for (x, y) in boggle[word[location]]:
			if abs(path[-1][0]-x) <= 1 and abs(path[-1][1]-y) <= 1:
				if (x, y) not in path:
					path.append((x, y))
					if correct_word(location+1, word, path, boggle) is True:
						return True
					else:
						path.pop()


if __name__ == '__main__':
	main()
