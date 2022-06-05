import random

words = ['cat', 'dog', 'mouse', 'cow', 'pig', 'goat', 'horse', 'chicken',
	'fox', 'wolf', 'snake', 'duck', 'sheep', 'ram']
word1 = words[random.randint(0, 14)]

def hangman(word):
	wrong = 0
	stages = ['',
			'__________         ',
			'|                  ',
			'|         |        ',
			'|         0        ',
			'|        /|\       ',
			'|        / \       ',
			'|                  '
			]
	rletters = list(word)
	board = ['__'] * len(word)
	win = False
	print('Welcome!')
	while wrong < len(stages) - 1:
		print('\n')
		msg = 'Enter character: '
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print((' '.join(board)))
		e = wrong + 1
		print('\n'.join(stages[0:e]))
		if '__' not in board:
			print('You win! There was word: ')
			print(' '.join(board))
			win = True
			break
	if not win:
		print('\n'.join(stages[0: wrong]))
		print('You failed! There was word: {}.'.format(word))

hangman(word1)
