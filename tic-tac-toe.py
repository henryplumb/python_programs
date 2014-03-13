#!/usr/env/python

# Tic-Tac-Toe by Henry Plumb

import random

board = [0,1,2,
		 3,4,5,
		 6,7,8]

def show_board():
	print('  ' + str(board[0]) + ' | ' + str(board[1]) + ' | ' + str(board[2]))
	print(' -----------')
	print('  ' + str(board[3]) + ' | ' + str(board[4]) + ' | ' + str(board[5]))
	print(' -----------')
	print('  ' + str(board[6]) + ' | ' + str(board[7]) + ' | ' + str(board[8]))

def check_line(char, s1, s2, s3):
	if board[s1] == char and board[s2] == char and board[s3] == char:
		return True

def check_board(char):
	if check_line(char, 0, 1, 2):
		return True
	if check_line(char, 3, 4, 5):
		return True
	if check_line(char, 6, 7, 8):
		return True
	if check_line(char, 0, 3, 6):
		return True
	if check_line(char, 1, 4, 7):
		return True
	if check_line(char, 2, 5, 8):
		return True
	if check_line(char, 0, 4, 8):
		return True
	if check_line(char, 2, 4, 6):
		return True

while True:
	loc = input('Select a square: ')
	loc = int(loc)

	if board[loc] != 'x' and board[loc] != 'o':
		board[loc] = 'x'

		if check_board('x') == True:
			print('-- X WINS! --')
			break;

		while True:

			random.seed()
			cpu_loc = random.randint(0,8)

			if board[cpu_loc] != 'o' and board[cpu_loc] != 'x':
				board[cpu_loc] = 'o'

				if check_board('o') == True:
					print('-- O WINS! --')
					break;

				break;

	else:
		print('This location is taken!')

	show_board()
