# 2048 clone by Henry Plumb (henry@android.net)

import curses
import random

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.nodelay(1)

board = [0,1,2,3,
		 4,5,6,7,
		 8,9,10,11,
		 12,13,14,15]

def showBoard():
	screen.addstr(0, 0, " | " + str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]) + " | " + str(board[3]) + " | ")
	screen.addstr(0, 1, "-----------------------")
	screen.addstr(0, 2, " | " + str(board[4]) + " | " + str(board[5]) + " | " + str(board[6]) + " | " + str(board[7]) + " | ")
	screen.addstr(0, 3, "-----------------------")
	screen.addstr(0, 4, " | " + str(board[8]) + " | " + str(board[9]) + " | " + str(board[10]) + " | " + str(board[11]) + " | ")
	screen.addstr(0, 5, "-----------------------")
	screen.addstr(0, 6, " | " + str(board[12]) + " | " + str(board[13]) + " | " + str(board[14]) + " | " + str(board[15]) + " | ")
	screen.addstr(0, 7, "-----------------------")

def moveTiles(dir):


def checkWin():
	for item in board:
		if item == "2048":
			return True
	return False

while True:
	char = screen.getch()

	if char == curses.KEY_UP:
		moveTiles("up")
	elif char == curses.KEY_DOWN:
		moveTiles("down")
	elif char == curses.KEY_LEFT:
		moveTiles("left")
	elif char == curses.KEY_RIGHT:
		moveTiles("right")

	if checkWin():
		screen.addstr(0, 1, "Congratulations! You have mastered 2048!")
		screen.refresh()

	screen.refresh()